"""
 Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
 """
"""
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

def post_email(q):
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    
    try:
        response = requests.post(url, data=data)
        response_json = response.json()

        if response.headers['content-type'] == 'application/json' and response_json:
            user_id = response_json.get('id')
            user_name = response_json.get('name')
            print("[{}] {}".format(user_id, user_name))
        elif not response_json:
            print("No result")
        else:
            print("Not a valid JSON")

    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    q = sys.argv[1]
    post_email(q)
