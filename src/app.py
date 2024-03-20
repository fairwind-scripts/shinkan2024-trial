from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return """<div>
    <h1>Hello, World!</h1>
    <p>Welcome to the Flask app</p>
    <a href="/template">Go to template</a>
    </div>
    """


@app.route("/template")
def hello() -> str:
    return render_template("hello.html")
