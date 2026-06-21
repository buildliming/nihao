"""
期末复习平台 — Flask 本地服务器
用法: python launcher.py
"""
import os
import sys
import webbrowser
import threading
from flask import Flask, send_from_directory

BASE = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

app = Flask(__name__, template_folder=os.path.join(BASE, "templates"))


def _send(path: str):
    """发送 templates 下的文件，自动补 index.html"""
    if path.endswith("/"):
        path += "index.html"
    return send_from_directory(app.template_folder, path)


# 静态资源优先匹配
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(os.path.join(BASE, "static"), filename)


# 首页
@app.route("/")
def index():
    return _send("index.html")


# 各科页面 (如 /高数大一下/学习/ → 高数大一下/学习/index.html)
@app.route("/<path:filename>")
def serve_page(filename):
    return _send(filename)


def main():
    url = f"http://127.0.0.1:{PORT}"

    def open_browser():
        webbrowser.open(url, new=2)

    threading.Timer(0.5, open_browser).start()

    print("=" * 48)
    print("   [期末复习平台]")
    print(f"   地址: {url}")
    print("   按 Ctrl+C 停止")
    print("=" * 48)
    for name in ["高数大一下 (学习|练习|考试)", "大学物理", "线性代数", "C语言"]:
        print(f"     {name}")
    print()

    app.run(host="127.0.0.1", port=PORT, debug=False)


if __name__ == "__main__":
    main()
