#!/usr/bin/python3
"""Script that, for a given employee ID, exports their TODO list
progress in CSV format.
"""
import csv
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

    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ])