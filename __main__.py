#!/usr/bin/env python3
"""
CAF Writing — 小说创作框架入口
"""
import sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)

if __name__ == "__main__":
    import argparse
    from dashboard.app import app
    from project_manager import list_projects, create_project

    parser = argparse.ArgumentParser(description="CAF Writing — 小说共创框架")
    parser.add_argument("--dashboard", action="store_true", help="启动 Dashboard")
    parser.add_argument("--port", type=int, default=8092, help="Dashboard 端口")
    parser.add_argument("--create", nargs=2, metavar=("NAME", "TITLE"), help="创建新项目")
    parser.add_argument("--list", action="store_true", help="列出项目")
    args = parser.parse_args()

    if args.create:
        name, title = args.create
        result = create_project(name=name, title=title)
        if "error" in result:
            print(f"❌ {result['error']}")
        else:
            print(f"✅ 作品「{title}」已创建 → projects/{name}/")
        sys.exit(0)

    if args.list:
        projects = list_projects()
        if not projects:
            print("📚 暂无项目")
        else:
            for p in projects:
                print(f"  {p['name']:20s} {p['title']:20s} {p.get('genre',''):10s} {p.get('word_count',0):>6d}字")
        sys.exit(0)

    # 默认启动 Dashboard
    print(f"\n  📖 CAF Writing — AI 共创小说框架")
    print(f"  Dashboard → http://0.0.0.0:{args.port}")
    print(f"  项目目录: projects/")
    print()
    app.run(host="0.0.0.0", port=args.port, debug=False)
