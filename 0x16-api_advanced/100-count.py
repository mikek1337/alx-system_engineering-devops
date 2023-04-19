#!/usr/bin/python3
import re
import requests
"""Simple module."""


def count_words(subreddit, word_list):
    """Counts words in the subreddit."""
    print(make_request(subreddit))
    print(word_list)


def count_subreddit(subreddit_content, word_list, count_tracker):
    if (len(word_list) == 0):
        return count_tracker
    word = word_list.pop()
    found = len(re.fullmatch(word, subreddit_content, re.IGNORECASE))
    if (found > 0):
        count_tracker[word] = int(count_tracker[word]) + found
        return count_subreddit(subreddit_content, word_list, count_tracker)


def make_request(subreddit):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       allow_redirects=False)

    if res.status_code != 200:
        return None
    return res.json()


