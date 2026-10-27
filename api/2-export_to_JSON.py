#!/usr/bin/python3
"""Export all tasks owned by an employee to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": user_id}).json()

    username = user.get("username")
    data = {
        user_id: [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username,
            }
            for todo in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile)
