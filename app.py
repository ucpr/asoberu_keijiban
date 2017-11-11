import json
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hoge():
    res = {
        "comment":[
            {
                "text":"hoge",
                "date":"hoge",
                "pic": ""
            },
            {
                "text":"hoge",
                "date":"hoge",
                "pic": ""
            }
        ]
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run()
