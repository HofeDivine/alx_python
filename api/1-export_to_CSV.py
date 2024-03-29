
import csv
import requests
import sys


def get_employee_info(employee_id):
    # Fetch employee details
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    user_id = user_data['id']
    username = user_data['username']

    # Fetch employee's TODO list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Write data to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in todo_data:
            writer.writerow([user_id, username, task['completed'], task['title']])
    print(f"Number of tasks in CSV: {len(todo_data)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [employee_id]")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)