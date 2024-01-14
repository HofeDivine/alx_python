"""Python script that takes in a URL and an email address, 
sends a POST request to the passed URL with the email 
as a parameter, and finally displays the body of the response"""
import requests
import sys

def send_post_request(url, email):
    try:
        # Data to be sent in the POST request
        data = {'email': email}

        # Send a POST request to the specified URL with the email parameter
        response = requests.post(url, data=data)

        # Display the body of the response
        print("Response body:")
        print(response.text)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt user for URL and email
    url = input("Enter the URL: ")
    email = input("Enter the email address: ")

    # Call the function to send the POST request and display the response
    send_post_request(url, email)
