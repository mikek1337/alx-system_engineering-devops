#!/usr/bin/python3

"""Get top ten hot subreddits"""

import requests


def top_ten(subreddit):
    headers = {"user-agent": "alx-project", "content-type": "application/json"}
    param = {"limit": "10"}
    res = requests.get("https://www.reddit.com/r/{}/hot/.json"
                       .format(subreddit), headers=headers)
