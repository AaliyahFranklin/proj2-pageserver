import os
from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def home():
    return "UOCIS docker demo!"

@app.route("/<path:name>")
def serve(name):
    if name.startswith("~") or name.startswith(".."):
        abort(403)
    if not os.path.isfile(os.path.join("templates", name)):
        abort(404)
    return render_template(name)

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def error_403(e):
    return render_template("403.html"), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
