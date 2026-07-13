#!/usr/bin/python3
"""Script that exports data of ALL employees' TODO list progress
to a JSON file, in a dictionary of list of dictionaries format.
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_res = requests.get("{}/users".format(base_url))
    users = users_res.json()

    todos_res = requests.get("{}/todos".format(base_url))
    todos = todos_res.json()

    all_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]
        all_data[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)