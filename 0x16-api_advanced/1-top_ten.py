#!/usr/bin/python3

"""Get top ten hot subreddits"""

import requests


def top_ten(subreddit):
    headers = {"user-agent": "alx-project", "content-type": "application/json"}
    param = {"limit": "10"}
    res = requests.get("https://www.reddit.com/r/{}/hot/.json"
                       .format(subreddit), headers=headers, params=param)
    json_result = res.json()
    data = json_result.get('data')
    children = data.get('children')
    print("\n".join([child.get('data').get('title') for child in children]))
