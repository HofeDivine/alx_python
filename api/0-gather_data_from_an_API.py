import requests
import sys


def get_employee_info(employee_id):
    # Fetch employee details
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch employee's TODO list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Calculate number of completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    # Print employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [employee_id]")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
