"""
Python script that takes in a URL, sends a request to the URL and displays the body of the response
"""
import requests
import sys
def error_code(url):
    response = requests.get(url)
    status_code = requests.status_codes
    if status_code <400:
        print(response.text)
    else:
        print("Error code: {}".format(status_code))
if __name__ == "__main__":
    if len(sys.argv) !=2:
        sys.exit(1)
    url =sys.argv[1]
    error_code(url)