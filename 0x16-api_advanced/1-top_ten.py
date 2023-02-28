#!/usr/bin/python3

"""Get top ten hot subreddits"""

import requests


def top_ten(subreddit):
    """Get top ten"""
    headers = {"user-agent": "alx-project", "content-type": "application/json"}
    param = {"limit": "10"}
    res = requests.get("https://www.reddit.com/r/{}/hot/.json"
                       .format(subreddit), headers=headers, params=param)
    if res.status_code == 404 or res.status_code == 301:
        print(None)
    json_result = res.json()
    data = json_result.get('data')
    children = data.get('children')
    print("\n".join([child.get('data').get('title') for child in children]))
