"""Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

def get_x_request_id(url):
    """Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""
    try:
        
        response = requests.get(url)

        
        if response.status_code == 200:
            
            x_request_id = response.headers.get('X-Request-Id')

            if x_request_id:
                print(f"{x_request_id}")
            
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
