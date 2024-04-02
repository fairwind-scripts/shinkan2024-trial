from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
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
