from pathlib import Path

from flask import Flask, render_template
from markdown import markdown

app = Flask(__name__)


@app.route("/")
def greet() -> str:
    return """<div>
    <h1>Hello, World!</h1>
    <p>Welcome to the Flask app</p>
    <a href="/sample">Go to sample page</a>
    </div>
    """


@app.route("/sample")
def sample() -> str:
    return render_template("sample.html")


@app.route("/materials")
def materials() -> str:
    return render_template("materials.html")


@app.route("/materials/platform")
def platform() -> str:
    with Path("src/static/md/platform.md").open(encoding="utf-8") as f:
        content = f.read()
    content = content.replace("../images/", "/static/images/")
    return render_template(
        "md_template.html",
        content=markdown(
            content,
            extensions=[
                "fenced_code",
                "codehilite",
            ],
        ),
    )


@app.route("/materials/hp")
def hp() -> str:
    return render_template("materials-hp.html")
