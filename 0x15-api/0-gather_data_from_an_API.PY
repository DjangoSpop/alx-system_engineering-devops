#!/usr/bin/python3
"""Script that returns to-do list information for a given employee ID."""
import requests
import sys

def get_tasks_for_employee(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    if not user:
        raise Exception(f"User with ID {employee_id} not found")
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    return todos

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        todos = get_tasks_for_employee(employee_id)
    except Exception as e:
        print(e)
        sys.exit(1)

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    num_completed = len(completed)
    if num_completed > 0:
        print(f"Employee {user.get('name')} is done with tasks"
              f"({num_completed}/{len(todos)})")
        for task in completed:
            print(f"\t{task}")
    else:
        print(f"Employee {user.get('name')} has no completed tasks")