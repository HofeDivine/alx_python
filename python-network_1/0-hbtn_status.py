"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import requests

def fetch_and_display_status(url):
   
    """Python script that fetches https://alu-intranet.hbtn.io/status"""
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Display the body of the response with tabulation
            print("Body response:")
            print("\t- type:", type(response.text))
            print("\t- content:", response.text)
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # URL to fetch
    url = "https://alu-intranet.hbtn.io/status"
    
    # Fetch and display the status
    fetch_and_display_status(url)
