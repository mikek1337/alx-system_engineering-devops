#!/usr/bin/python3
"""# Making contact with an API."""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
        res = requests.get(
            "https://jsonplaceholder.typicode.com/users/{id}".format(id=id))
        user_json = res.json()
        res = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={id}"
            .format(id=id))
        todos_json = res.json()
        todo_cus_json = dict()
        detail = dict()
        todo_cus_json[str(user_json["id"])] = list()

        for todo in todos_json:
            detail["task"] = todo["title"]
            detail["completed"] = todo["completed"]
            detail["username"] = user_json["name"]
            todo_cus_json[str(user_json["id"])].append(detail)
        file = open(str(user_json["id"])+".json", "w")
        json.dump(todo_cus_json, file)
