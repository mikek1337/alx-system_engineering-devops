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
        file = open(str(user_json["id"])+".csv", "w")
        for todo in todos_json:
            file.write('"' + str(user_json['id']) + '","' + user_json['username'] + '","' + str(todo['completed']) + '","' + todo['title'] + '"\n')

        file.close()
