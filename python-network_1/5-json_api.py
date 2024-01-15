"""
 Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
 """

import requests
import sys

def search_user(letter):
    try:
        url = "http://0.0.0.0:5000/search_user"
        data = {'q': letter}
        response = requests.post(url, data=data)

        # Print raw response content for debugging
        print("Raw Response Content:", response.content)

        if response.headers['content-type'] == 'application/json' and response.json():
            user_data = response.json()
            user_id = user_data.get('id')
            user_name = user_data.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            if not response.json():
                print("No result")
            else:
                print("Not a valid JSON")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    # Call the function to send the POST request and display the response
    search_user(letter)
