#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(
        "{}users/{}".format(base_url, employee_id)
    )
    todos_response = requests.get(
        "{}todos".format(base_url),
        params={"userId": employee_id}
    )

    user_response.raise_for_status()
    todos_response.raise_for_status()

    employee = user_response.json()
    todos = todos_response.json()

    tasks = [
        {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": employee["username"]
        }
        for todo in todos
    ]

    with open("{}.json".format(employee_id), "w",
              encoding="utf-8") as json_file:
        json.dump({str(employee_id): tasks}, json_file)
