import json
import os
import requests
from requests_oauthlib import OAuth1


class Twitter:
    URL = "https://api.twitter.com/1.1/search/tweets.json"

    def __init__(self):
        self.auth = self._create_auth()

    def _create_auth(self):
        """ authを返すお """
        auth = OAuth1(
            os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"],
            os.environ["TOKEN"], os.environ["TOKEN_SECRET"]
        )
        return auth

    def get_comment(self, hash_tag):
        params = {"q": "#"+hash_tag, "count": "100"}
        req = requests.get(self.URL, auth=self.auth, params=params)
        for i in req.iter_lines():
            data = json.loads(i)
            json_data = self.create_json(data, len(data["statuses"]))
            with open("comment.json", "w") as f:
                json.dump(json_data, f)

    def create_json(self, data, length):
        res = {"comment": [{} for i in range(length)]}
        for i in range(length):
            pic = data["statuses"][i]["entities"]  # ここからpicのurlを
            date = data["statuses"][i]["created_at"]  # 日付
            text = data["statuses"][i]["text"].split()[1]  # tweetの本文
            print(pic, text)

            res["comment"][i]["text"] = text
            res["comment"][i]["date"] = date
            res["comment"][i]["pic"] = pic
        return res


if __name__ == "__main__":
    tw = Twitter()
    tw.get_comment("#遊べる掲示板")
