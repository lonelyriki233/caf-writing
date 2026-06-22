"""
CAF Writing — 项目管理器
创建、加载、继承、查询项目。每个作品为一个独立项目。
"""
import os
import json
import shutil
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
PROJECTS_DIR = os.path.join(BASE, "projects")
TEMPLATES_DIR = os.path.join(BASE, "templates")

# 项目结构模板
PROJECT_SCAFFOLD = {
    "world": "世界观设定",
    "characters": "人物档案",
    "plot": "剧情脉络",
    "chapters": "章节正文",
}


def list_projects():
    """列出所有项目"""
    if not os.path.exists(PROJECTS_DIR):
        return []
    projects = []
    for name in sorted(os.listdir(PROJECTS_DIR)):
        meta_path = os.path.join(PROJECTS_DIR, name, "meta.json")
        if os.path.isfile(meta_path):
            with open(meta_path, encoding="utf-8") as f:
                meta = json.load(f)
            projects.append(meta)
    return projects


def get_project(name):
    """获取单个项目元数据"""
    meta_path = os.path.join(PROJECTS_DIR, name, "meta.json")
    if not os.path.exists(meta_path):
        return None
    with open(meta_path, encoding="utf-8") as f:
        return json.load(f)


def create_project(name, title="", genre="", logline="", template="new_project"):
    """创建新项目"""
    project_dir = os.path.join(PROJECTS_DIR, name)

    if os.path.exists(project_dir):
        return {"error": f"项目已存在: {name}"}

    # 创建目录结构
    os.makedirs(project_dir, exist_ok=True)
    for subdir in PROJECT_SCAFFOLD:
        os.makedirs(os.path.join(project_dir, subdir), exist_ok=True)

    # 元数据
    now = datetime.now().isoformat()
    meta = {
        "name": name,
        "title": title or name,
        "genre": genre,
        "logline": logline,
        "created": now,
        "updated": now,
        "status": "active",
        "progress": 0,
        "word_count": 0,
        "character_count": 0,
        "chapter_count": 0,
    }
    with open(os.path.join(project_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    # 初始化空文件
    for dir_name, label in PROJECT_SCAFFOLD.items():
        readme = os.path.join(project_dir, dir_name, "README.md")
        if not os.path.exists(readme):
            with open(readme, "w", encoding="utf-8") as f:
                f.write(f"# {title} — {label}\n\n*空，等待填充*\n")

    # 时间线
    timeline = os.path.join(project_dir, "timeline.md")
    if not os.path.exists(timeline):
        with open(timeline, "w", encoding="utf-8") as f:
            f.write(f"# {title} 时间线\n\n| 时间 | 事件 | 备注 |\n|------|------|------|\n")

    return meta


def update_meta(name, **kwargs):
    """更新项目元数据"""
    meta = get_project(name)
    if not meta:
        return None
    for k, v in kwargs.items():
        if v is not None:
            meta[k] = v
    meta["updated"] = datetime.now().isoformat()
    meta_path = os.path.join(PROJECTS_DIR, name, "meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    return meta


def count_words(name):
    """统计项目字数"""
    project_dir = os.path.join(PROJECTS_DIR, name)
    total = 0
    chapters_dir = os.path.join(project_dir, "chapters")
    if os.path.exists(chapters_dir):
        for fname in os.listdir(chapters_dir):
            fpath = os.path.join(chapters_dir, fname)
            if fname.endswith(".md") and os.path.isfile(fpath):
                with open(fpath, encoding="utf-8") as f:
                    total += len(f.read())
    update_meta(name, word_count=total, chapter_count=len([
        f for f in os.listdir(chapters_dir) if f.endswith(".md")
    ]) if os.path.exists(chapters_dir) else 0)
    return total


def load_context(name):
    """加载项目全部上下文（给 agent 用）"""
    meta = get_project(name)
    if not meta:
        return None
    project_dir = os.path.join(PROJECTS_DIR, name)
    context = {"meta": meta, "world": "", "characters": "", "plot": "", "timeline": ""}

    for key, path_key in [("world", "world"), ("characters", "characters"), ("plot", "plot")]:
        readme = os.path.join(project_dir, path_key, "README.md")
        if os.path.exists(readme):
            with open(readme, encoding="utf-8") as f:
                context[key] = f.read()

    tl = os.path.join(project_dir, "timeline.md")
    if os.path.exists(tl):
        with open(tl, encoding="utf-8") as f:
            context["timeline"] = f.read()

    return context
