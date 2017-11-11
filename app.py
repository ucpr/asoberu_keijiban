import json
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hoge():
    with open("comment.json", "r") as f:
        f = json.load(f)
    return jsonify(f)


if __name__ == "__main__":
    app.run()
