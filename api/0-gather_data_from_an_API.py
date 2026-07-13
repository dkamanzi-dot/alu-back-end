#!/usr/bin/python3
"""Script that, for a given employee ID, returns information about
his/her TODO list progress, using a REST API.
"""
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

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))