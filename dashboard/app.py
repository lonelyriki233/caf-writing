from flask import Flask, render_template, request, jsonify
import sys, os

# 确保能找到 project_manager 和 context_db
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from project_manager import list_projects, get_project, create_project, update_meta, count_words, load_context
from context_db import ContextDB

app = Flask(__name__)
app.config["TEMPLATE_FOLDER"] = os.path.join(os.path.dirname(__file__), "templates")


@app.route("/")
def index():
    projects = list_projects()
    return render_template("index.html", projects=projects)


@app.route("/project/<name>")
def project_detail(name):
    meta = get_project(name)
    if not meta:
        return "项目不存在", 404
    project_dir = os.path.join(os.path.dirname(__file__), "projects", name)
    db = ContextDB(project_dir)
    context = load_context(name)
    summary = db.get_summary()
    events = db.get_arc()
    return render_template("project.html",
                           meta=meta, context=context,
                           summary=summary, events=events)


@app.route("/api/projects")
def api_projects():
    return jsonify(list_projects())


@app.route("/api/projects", methods=["POST"])
def api_create():
    data = request.json
    result = create_project(
        name=data.get("name"),
        title=data.get("title", ""),
        genre=data.get("genre", ""),
        logline=data.get("logline", ""),
    )
    if "error" in result:
        return jsonify(result), 400
    return jsonify(result), 201


@app.route("/api/project/<name>")
def api_project(name):
    meta = get_project(name)
    if not meta:
        return jsonify({"error": "not found"}), 404
    context = load_context(name)
    return jsonify({"meta": meta, "context": context})


@app.route("/api/project/<name>/context")
def api_context(name):
    context = load_context(name)
    if not context:
        return jsonify({"error": "not found"}), 404
    db_dir = os.path.join(os.path.dirname(__file__), "projects", name, "db")
    os.makedirs(db_dir, exist_ok=True)
    return jsonify(context)


@app.route("/api/project/<name>/summary")
def api_summary(name):
    meta = get_project(name)
    if not meta:
        return jsonify({"error": "not found"}), 404
    project_dir = os.path.join(os.path.dirname(__file__), "projects", name)
    db = ContextDB(project_dir)
    summary = db.get_summary()
    return jsonify({"meta": meta, "summary": summary})


if __name__ == "__main__":
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 8092))
    sock.close()
    port = 8092 if result != 0 else 8093
    print(f"  CAF Writing Dashboard → http://0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
