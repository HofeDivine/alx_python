"""Write a Python script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id"""
import requests
import sys

def get_github_user_id(username, password):
    url = "https://api.github.com/user"

    # Use Basic Authentication with the provided username and personal access token
    auth = (username, password)

    # Send a GET request to the GitHub API
    response = requests.get(url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        user_data = response.json()
        
        # Display the user ID
        print("Your GitHub user ID: {}".format(user_data['id']))
    else:
        # Display an error message
        print("Error accessing GitHub API. Status code: {}".format(response.status_code))

if __name__ == "__main__":
    # Get GitHub credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Call the function to retrieve and display the GitHub user ID
    get_github_user_id(username, password)

