
import sys
import requests
import typing
import urllib
#whats suprvised learning ?
#whats unsupervised learning ?
def get_user(user_id: int) -> typing.Dict:
    """Fetch user data from the API."""
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url + f"{user_id}")
    response.raise_for_status()
    return response.json()

def get_tasks_for_employee(employee_id: int) -> typing.List[typing.Dict]:
    """Fetch tasks for a given employee ID."""
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": employee_id}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
def get_user_data(user_id):
    """Fetch user data from the API."""
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url + f"{user_id}")
    response.raise_for_status()
    return response.json()

def get_completed_tasks_titles(todos: typing.List[typing.Dict]) -> typing.List[str]:
    """Return a list of completed tasks' titles."""
    return [todo["title"] for todo in todos if todo.get("completed", False)]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print(f"Invalid employee ID: {employee_id} should be an integer.")
        sys.exit(1)

    try:
        user = get_user(employee_id)
        todos = get_tasks_for_employee(employee_id)
    except requests.exceptions.HTTPError as e:
        print(e)
        sys.exit(1)

    completed_tasks = get_completed_tasks_titles(todos)
    num_completed = len(completed_tasks)

    if num_completed > 0:
        print(f"{num_completed} tasks were completed:")
        print("\n".join(completed_tasks))