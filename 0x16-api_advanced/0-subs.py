#!/usr/bin/python3

"""Get subs from reddit"""
import requests


def number_of_subscribers(subreddit):
    headers = {'user-agent': 'lickme', 'content-type': 'application/json'}
    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers=headers)
    result = res.json()
    if res.status_code != 404:
        return result.get('data').get('subscribers')
    return 0
