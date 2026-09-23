from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    msg = data["message"]

    return {
        "reply": f"Server received: {msg}"
    }
