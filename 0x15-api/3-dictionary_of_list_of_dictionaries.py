#!/usr/bin/python3
"""# Making contact with an API."""

import json
import requests


if __name__ == "__main__":
    res = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    user_json = res.json()
    file = open("todo_all_employees.json", "w")
    todo_cus_json = dict()
    for user in user_json:
        res = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={id}"
            .format(id=user["id"]))
        todos_json = res.json()
        detail = dict()
        todo_cus_json[str(user["id"])] = list()

        for todo in todos_json:
            detail["username"] = user["name"]
            detail["task"] = todo["title"]
            detail["completed"] = todo["completed"]
            todo_cus_json[str(user["id"])].append(detail)
    json.dump(todo_cus_json, file)
