import json
import os
import requests
from requests_oauthlib import OAuth1


class Twitter:
    URL = "https://api.twitter.com/1.1/search/tweets.json"

    def __init__(self, hashtag):
        self.auth = self._create_auth()
        self.hash_tag = hashtag

    def _create_auth(self):
        """ authを返すお """
        auth = OAuth1(
            os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"],
            os.environ["TOKEN"], os.environ["TOKEN_SECRET"]
        )
        return auth

    def _create_json(self, data, length):
        res = {"comment": [{} for i in range(length)]}
#        print(data["statuses"])
        for i in range(length):
            pic = data["statuses"][i]["entities"]  # ここからpicのurlを
            date = data["statuses"][i]["created_at"]  # 日付
            text = data["statuses"][i]["text"]  # tweetの本文
            if "media" not in pic.keys():
                pic = ""
                text = self._text_format(text, False)
            else:
                pic = pic["media"][0]["media_url_https"]
                text = self._text_format(text)

            if not self._over_40(text):  # 40文字以上だったら35文字目まで + "..."
                text = text[:35] + "..."
            print(text)

            res["comment"][i]["text"] = text
            res["comment"][i]["date"] = date
            res["comment"][i]["pic"] = pic

        return res

    def _text_format(self, text, pic=True):
        if pic:
            text = text.split()[:-1]  # 画像のlinkを消す
            if text[0] == "#"+self.hash_tag:
                text.pop(0)
            elif text[-1] == "#"+self.hash_tag:
                text.pop(len(text)-1)
        else:
            text = text.split()
            if text[0] == "#"+self.hash_tag:
                text.pop(0)
            elif text[-1] == "#"+self.hash_tag:
                text.pop(len(text)-1)

        text = " ".join(text)
        if len(text) > 20:  # 20文字より多かったら改行を入れる
            text = list(text)
            text.insert(20, "<br>")
            text = "".join(text)

        return text

    def _over_40(self, text):
        """ commentが40文字を超えていたらだめ """
        if len(text) >= 45:  # <br>を含むため45に
            return False
        return True

    def get_comment(self):
        params = {"q": "#"+self.hash_tag, "count": "15"}
        req = requests.get(self.URL, auth=self.auth, params=params)
        for i in req.iter_lines():
            data = json.loads(i)
            json_data = self._create_json(data, len(data["statuses"]))
            with open("comment.json", "w") as f:
                json.dump(json_data, f)  # jsonに書き込み


if __name__ == "__main__":
    tw = Twitter()
    tw.get_comment("#遊べる掲示板")
