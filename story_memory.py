"""
CAF Writing — 故事记忆数据库
用 Embedding + ChromaDB 持久化故事信息，实现：
- 人物档案语义检索（"和主角有冲突的配角是谁"）
- 剧情事件追溯（"第三章发生了什么"）
- 章节内容搜索（"描写过那个遗迹的什么细节"）
- 人物决策模式分析

当作品内容超过上下文窗口时自动接管。
"""
import os
import json
import chromadb
import urllib.request
from typing import Optional


def _get_embedding_api_key():
    """从 .hermes/.env 读取 embedding key"""
    env_path = os.path.expanduser("~/.hermes/.env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    if k.strip() == "XFYUN_EMBEDDING_KEY":
                        return v.strip().strip('"').strip("'")
    return ""


EMBEDDING_KEY = _get_embedding_api_key()
EMBEDDING_URL = "https://maas-api.cn-huabei-1.xf-yun.com/v2/embeddings"
EMBEDDING_MODEL = "xop3qwen8bembedding"


def get_embedding(texts: list[str]) -> list[list[float]]:
    """调用 xfyun embedding API"""
    if not EMBEDDING_KEY:
        raise RuntimeError("XFYUN_EMBEDDING_KEY 未配置")
    payload = json.dumps({"model": EMBEDDING_MODEL, "input": texts}).encode()
    req = urllib.request.Request(
        EMBEDDING_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + EMBEDDING_KEY,
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        resp = json.loads(r.read().decode())
    return [d["embedding"] for d in resp["data"]]


class StoryMemory:
    """故事记忆数据库，每个项目独立实例"""

    def __init__(self, project_dir: str):
        self.project_dir = project_dir
        self.db_path = os.path.join(project_dir, "db", "story_memory")
        os.makedirs(self.db_path, exist_ok=True)

        self.client = chromadb.PersistentClient(path=self.db_path)
        self._init_collections()

    def _init_collections(self):
        """初始化不同维度的集合"""
        self.collections = {}
        for name in ["characters", "events", "chapters", "worldbuilding", "decisions"]:
            try:
                self.collections[name] = self.client.get_collection(name)
            except:
                self.collections[name] = self.client.create_collection(
                    name=name,
                    metadata={"hnsw:space": "cosine"},
                )

    # === 写入 ===

    def index_character(self, char_id: str, name: str, traits: str,
                        background: str, role: str, relationships: str = ""):
        """索引人物档案"""
        text = f"人物：{name}\n身份：{role}\n性格：{traits}\n背景：{background}\n关系：{relationships}"
        self._add("characters", char_id, text, {
            "type": "character", "name": name, "role": role,
            "traits": traits, "relationships": relationships,
        })

    def index_event(self, event_id: str, title: str, description: str,
                    chapter: int, characters: list[str], impact: str = ""):
        """索引剧情事件"""
        text = f"事件：{title}\n描述：{description}\n涉及人物：{', '.join(characters)}\n影响：{impact}"
        self._add("events", event_id, text, {
            "type": "event", "title": title, "chapter": chapter,
            "characters": json.dumps(characters, ensure_ascii=False),
        })

    def index_chapter(self, chapter_num: int, title: str, content: str):
        """索引章节内容（按段落分块）"""
        # 每 500 字为一块
        chunks = []
        for i in range(0, len(content), 500):
            chunk = content[i:i + 500]
            chunk_id = f"ch{chapter_num}_p{i // 500}"
            chunks.append((chunk_id, chunk, {
                "type": "chapter_section", "chapter": chapter_num,
                "title": title, "offset": i,
            }))

        if not chunks:
            return

        texts = [c[1] for c in chunks]
        embeddings = get_embedding(texts)
        self.collections["chapters"].add(
            documents=texts,
            embeddings=embeddings,
            metadatas=[c[2] for c in chunks],
            ids=[c[0] for c in chunks],
        )

    def index_world(self, section_id: str, section_title: str, content: str):
        """索引世界观设定"""
        self._add("worldbuilding", section_id, f"{section_title}\n{content}", {
            "type": "worldbuilding", "title": section_title,
        })

    def index_decision(self, decision_id: str, char_name: str,
                       context: str, decision: str, reasoning: str):
        """索引人物决策"""
        text = f"人物：{char_name}\n情境：{context}\n决策：{decision}\n理由：{reasoning}"
        self._add("decisions", decision_id, text, {
            "type": "decision", "character": char_name,
            "context": context, "decision": decision,
        })

    def _add(self, collection: str, doc_id: str, text: str, metadata: dict):
        """通用添加（单条）"""
        embedding = get_embedding([text])[0]
        self.collections[collection].add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[doc_id],
        )

    # === 读取 ===

    def search(self, collection: str, query: str, n: int = 5) -> list[dict]:
        """语义搜索"""
        query_vec = get_embedding([query])[0]
        results = self.collections[collection].query(
            query_embeddings=[query_vec],
            n_results=n,
        )
        items = []
        for i in range(len(results["ids"][0])):
            items.append({
                "id": results["ids"][0][i],
                "text": results["documents"][0][i][:300],
                "score": 1 - results["distances"][0][i],
                "metadata": results["metadatas"][0][i],
            })
        return sorted(items, key=lambda x: x["score"], reverse=True)

    def search_all(self, query: str, n: int = 3) -> dict[str, list]:
        """在所有维度搜索"""
        return {
            col: self.search(col, query, n)
            for col in self.collections
        }

    def get_character_decisions(self, char_name: str) -> list[dict]:
        """获取某个人物的所有决策记录"""
        results = self.collections["decisions"].query(
            query_texts=[f"人物：{char_name}"],
            n_results=20,
        )
        items = []
        for i in range(len(results["ids"][0])):
            meta = results["metadatas"][0][i]
            if meta.get("character") == char_name:
                items.append({
                    "id": results["ids"][0][i],
                    "context": meta.get("context", ""),
                    "decision": meta.get("decision", ""),
                })
        return items

    def get_summary(self) -> dict:
        """数据库统计"""
        return {
            "characters": self.collections["characters"].count(),
            "events": self.collections["events"].count(),
            "chapter_sections": self.collections["chapters"].count(),
            "worldbuilding": self.collections["worldbuilding"].count(),
            "decisions": self.collections["decisions"].count(),
        }
