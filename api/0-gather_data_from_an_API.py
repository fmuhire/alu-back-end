#!/usr/bin/python3
"""Gather data from an API for an employee's TODO list."""

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

    completed_tasks = [
        task for task in todos if task["completed"]
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee["name"], len(completed_tasks), len(todos)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
