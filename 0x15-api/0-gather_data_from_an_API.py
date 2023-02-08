#!/usr/bin/python3
"""# Making contact with an API."""


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

        def count_completed(x, y=0):
            if x['completed']:
                y += 1
            return y
        completed = list(map(count_completed, todos_json)).count(1)
        print("Employee {name} is done with tasks({completed}/{total}): "
              .format(name=user_json['name'], completed=completed, total=len(todos_json)))
        for todo in todos_json:
            if todo['completed']:
                print("\t {title}".format(title=todo['title']))
