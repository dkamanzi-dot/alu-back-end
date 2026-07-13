#!/usr/bin/python3
"""Script that, for a given employee ID, exports their TODO list
progress in JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_res = requests.get("{}/users/{}".format(base_url, employee_id))
    user = user_res.json()
    employee_name = user.get("name")

    todos_res = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )
    todos = todos_res.json()

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        }
        for task in todos
    ]

    data = {str(employee_id): tasks}

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)