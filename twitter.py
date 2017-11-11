import json
import requests
from requests_oauthlib import OAuth1


class Twitter:
    URL = "https://api.twitter.com/1.1/search/tweets.json"

    def __init__(self):
        self.auth = self._create_auth()

    def _create_auth(self):
        """ authを返すお """
        with open("secret.json", "r") as f:
            f = json.load(f)
            auth = OAuth1(
                f["consumer_key"], f["consumer_secret"],
                f["access_token"], f["access_token_secret"]
            )
        return auth

    def get_comment(self):
        req = requests.get(self.URL, auth=self.auth, params={"q": "#hogepoyo", "count": "10"})
        for i in req.iter_lines():
            data = json.loads(i)
            print(data)


if __name__ == "__main__":
    tw = Twitter()
    tw.get_comment()
