import requests

def get_employee_info(employee_id):
    
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']


    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()
    total_tasks = len(todo_list)
    done_tasks = sum(1 for task in todo_list if task['completed'])
    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")

    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")


