
import argparse
import requests from pythoncom

def get_employee_todo_progress(employee_id):
    """
    Retrieves the progress of an employee's TODO list based on the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee data
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()

    if not employee_data:
        print(f"No employee found with ID {employee_id}")
        return

    employee_name = employee_data["name"]

    # Get completed tasks for the employee
    completed_tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}&completed=true")
    completed_tasks_data = completed_tasks_response.json()

    # Get total tasks for the employee
    total_tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    total_tasks_data = total_tasks_response.json()

    number_of_done_tasks = len(completed_tasks_data)
    total_number_of_tasks = len(total_tasks_data)

    return employee_name, number_of_done_tasks, total_number_of_tasks

def print_employee_todo_progress(employee_name, number_of_done_tasks, total_number_of_tasks):
    """
    Prints the progress of an employee's TODO list in the required format.

    Args:
        employee_name (str): The name of the employee.
        number_of_done_tasks (int): The number of completed tasks.
        total_number_of_tasks (int): The total number of tasks.

    Returns:
        None
    """
    print(f"\nEmployee {employee_name} is done with tasks:")
    for _ in range(number_of_done_tasks):
        print(f"\t- [Task {_ + 1}]: Not specified")

    print(f"\nTotal number of tasks: {total_number_of_tasks}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get an employee's TODO list progress.")
    parser.add_argument("employee_ids", metavar="ID", type=int, nargs="+",
                        help="The IDs of the employees separated by spaces.")
    args = parser.parse_args()

    for employee_id in args.employee_ids:
        employee_name, number_of_done_tasks, total_number_of_tasks = get_employee_todo_progress(employee_id)
        if employee_name:
            print_employee_todo_progress(employee_name, number_of_done_tasks, total_number_of_tasks)