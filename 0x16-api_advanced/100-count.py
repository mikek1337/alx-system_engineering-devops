#!/usr/bin/python3

import requests
"""Simple module."""


def count_words(subreddit, word_list):
    """Counts words in the subreddit."""
    subreddit_content = make_request(subreddit).get("data").get("children")
    titles = collect_titles(subreddit_content, [])
    print(word_list)
    return count_subreddit(titles, word_list, {})


def count_subreddit(titles, word_list, count_tracker):
    if (len(titles) == 0):
        return count_tracker
    title = titles.pop()
    words = word_list
    print(count_exist(words, title, 0, 0))
    return count_subreddit(titles, word_list, count_tracker)


def count_exist(word_list, title, count, index):
    if (len(word_list) == index):
        return count
    title = title.lower()
    word = word_list[index].lower()
    count += title.count(word)
    index += 1
    return count_exist(word_list, title, count, index)


def collect_titles(children, titles):
    if (len(children) == 0):
        return titles
    child = children.pop()
    title = child.get("data").get("title")
    titles.append(title)
    return collect_titles(children, titles)


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


