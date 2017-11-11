import json
from flask import Flask, jsonify
import twitter

app = Flask(__name__)


@app.route("/comment/<hash_tag>", methods=["GET"])
def return_comment(hash_tag):
    """ GET reqがきたらjsonを返してあげたい気持ちでいっぱい """
    tw = twitter.Twitter(hash_tag)
    tw.get_comment()

    with open("comment.json", "r") as f:
        f = json.load(f)
    return jsonify(f)


if __name__ == "__main__":
    app.run()
