"""
CAF Writing — Agent 桥接器
供 Hermes / Agent 调用的接口：管理项目、读写内容、记录决策。
"""
import sys, os, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from project_manager import (
    list_projects, get_project, create_project,
    update_meta, load_context, count_words, PROJECTS_DIR
)
from context_db import ContextDB
from story_memory import StoryMemory


def agent_get_projects():
    """Agent 入口：获取所有作品列表"""
    return list_projects()


def agent_open_project(name):
    """Agent 入口：打开一个作品，返回完整上下文"""
    meta = get_project(name)
    if not meta:
        return {"error": f"项目 {name} 不存在。可用 create_project 创建。"}
    context = load_context(name)
    return {"meta": meta, "context": context}


def agent_create_project(name, title="", genre="", logline=""):
    """Agent 入口：创建新作品"""
    result = create_project(name=name, title=title, genre=genre, logline=logline)
    if "error" in result:
        return result
    return {"message": f"项目「{title or name}」已创建", "meta": result}


def agent_save_world(name, content):
    """保存/更新世界观设定"""
    path = os.path.join(PROJECTS_DIR, name, "world", "README.md")
    if not os.path.exists(os.path.dirname(path)):
        return {"error": f"项目 {name} 不存在"}
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    update_meta(name, updated=__import__("datetime").datetime.now().isoformat())
    return {"message": "世界观已更新", "word_count": len(content)}


def agent_save_character(name, content):
    """保存/更新人物档案"""
    path = os.path.join(PROJECTS_DIR, name, "characters", "README.md")
    if not os.path.exists(os.path.dirname(path)):
        return {"error": f"项目 {name} 不存在"}
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    update_meta(name)
    return {"message": "人物档案已更新"}


def agent_save_plot(name, content):
    """保存/更新剧情脉络"""
    path = os.path.join(PROJECTS_DIR, name, "plot", "README.md")
    if not os.path.exists(os.path.dirname(path)):
        return {"error": f"项目 {name} 不存在"}
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    update_meta(name)
    return {"message": "剧情脉络已更新"}


def agent_add_chapter(name, chapter_num, content):
    """添加或更新章节"""
    project_dir = os.path.join(PROJECTS_DIR, name)
    chapters_dir = os.path.join(project_dir, "chapters")
    os.makedirs(chapters_dir, exist_ok=True)
    filename = f"第{chapter_num}章.md"
    path = os.path.join(chapters_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# 第{chapter_num}章\n\n{content}")
    count_words(name)
    update_meta(name)
    return {"message": f"第{chapter_num}章已保存", "path": path}


def agent_analyze_character(name, char_id, char_name, traits, background=""):
    """Agent：创建人物并初始化心理模型"""
    project_dir = os.path.join(PROJECTS_DIR, name)
    db = ContextDB(project_dir)
    db.add_character(char_id, char_name, traits, "主角" if char_id == "protagonist" else "配角", background)

    # 同步到人物文档
    chars_path = os.path.join(project_dir, "characters", "README.md")
    with open(chars_path, "a", encoding="utf-8") as f:
        f.write(f"\n\n## {char_name}（{char_id}）\n- 性格：{traits}\n- 背景：{background}\n- 目标：待设定\n")

    # 更新人物数
    chars = db.load("characters")
    update_meta(name, character_count=len(chars))
    return {
        "message": f"人物「{char_name}」已创建",
        "prediction": db.predict_character_response(char_id, "初始场景"),
    }


def agent_record_decision(name, char_id, context, decision, reasoning=""):
    """Agent：记录人物在关键时刻的决策"""
    project_dir = os.path.join(PROJECTS_DIR, name)
    db = ContextDB(project_dir)
    db.add_decision(char_id, context, decision, reasoning)
    return {"message": f"已记录 {char_id} 的决策「{decision[:30]}..."}


def agent_analysis(name, question=""):
    """Agent：综合上下文 + 人物分析"""
    meta = get_project(name)
    if not meta:
        return {"error": "项目不存在"}
    project_dir = os.path.join(PROJECTS_DIR, name)
    context = load_context(name)
    db = ContextDB(project_dir)
    summary = db.get_summary()

    # 收集人物决策模式
    chars = db.load("characters")
    character_profiles = []
    for cid, c in chars.items():
        pattern = db._get_decision_pattern(chars, cid)
        character_profiles.append({
            "name": c.get("name", cid),
            "id": cid,
            "role": c.get("role", ""),
            "traits": c.get("traits", ""),
            "decision_pattern": pattern,
            "decisions_count": len(c.get("decisions", [])),
        })

    return {
        "meta": meta,
        "summary": summary,
        "character_profiles": character_profiles,
        "context_summary": {
            "world_len": len(context.get("world", "")),
            "characters_len": len(context.get("characters", "")),
            "plot_len": len(context.get("plot", "")),
        },
    }

def agent_index_all(name):
    """将项目全部故事内容索引到向量数据库（创作中后期使用）"""
    meta = get_project(name)
    if not meta:
        return {"error": "项目不存在"}
    project_dir = os.path.join(PROJECTS_DIR, name)
    context = load_context(name)
    sm = StoryMemory(project_dir)
    stats = {"characters": 0, "events": 0, "chapters": 0, "world": 0}

    # 索引人物档案
    chars_path = os.path.join(project_dir, "characters", "README.md")
    if os.path.exists(chars_path):
        with open(chars_path, encoding="utf-8") as f:
            content = f.read()
        sm.index_world("characters_all", "人物档案全集", content)
        stats["characters"] = 1

    # 索引世界观
    world_path = os.path.join(project_dir, "world", "README.md")
    if os.path.exists(world_path):
        with open(world_path, encoding="utf-8") as f:
            content = f.read()
        sm.index_world("world_all", "世界观设定", content)
        stats["world"] = 1

    # 索引剧情
    plot_path = os.path.join(project_dir, "plot", "README.md")
    if os.path.exists(plot_path):
        with open(plot_path, encoding="utf-8") as f:
            content = f.read()
        sm.index_world("plot_all", "剧情脉络", content)
        stats["world"] += 1

    # 索引各章节
    chapters_dir = os.path.join(project_dir, "chapters")
    if os.path.exists(chapters_dir):
        for fname in sorted(os.listdir(chapters_dir)):
            if fname.endswith(".md"):
                ch_path = os.path.join(chapters_dir, fname)
                with open(ch_path, encoding="utf-8") as f:
                    content = f.read()
                import re
                m = re.search(r'\d+', fname)
                ch_num = int(m.group()) if m else 0
                sm.index_chapter(ch_num, fname.replace(".md", ""), content)
                stats["chapters"] += 1

    # 读取上下文数据库
    from context_db import ContextDB
    cdb = ContextDB(project_dir)
    chars = cdb.load("characters")
    events = cdb.load("plot_events")
    for cid, c in chars.items():
        sm.index_character(cid, c.get("name", cid), c.get("traits", ""),
                          c.get("background", ""), c.get("role", ""),
                          json.dumps(c.get("relationships", {}), ensure_ascii=False))
        stats["characters"] += 1
        for d in c.get("decisions", []):
            sm.index_decision(f"{cid}_{d.get('timestamp','')}",
                             c.get("name", cid),
                             d.get("context", ""), d.get("decision", ""),
                             d.get("reasoning", ""))
    if isinstance(events, dict):
        for eid, e in events.items():
            sm.index_event(eid, e.get("title", ""), e.get("description", ""),
                          e.get("chapter", 0), e.get("characters", []),
                          e.get("impact", ""))
    return {"message": "故事记忆索引完成", "stats": stats, "memory_summary": sm.get_summary()}

def agent_search_memory(name, query, n=5):
    """搜索故事记忆数据库"""
    project_dir = os.path.join(PROJECTS_DIR, name)
    sm = StoryMemory(project_dir)
    return sm.search_all(query, n)
