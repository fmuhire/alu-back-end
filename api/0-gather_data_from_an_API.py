#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": employee_id}).json()

    done = [todo for todo in todos if todo.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for todo in done:
        print("\t {}".format(todo.get("title")))
