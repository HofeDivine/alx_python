"""
 Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
 """
import requests
import sys
def post_email(q):
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url,q)
    if response.headers['content-type'] =='application/json' and response.json():
        user_data = response.json
        user_id = user_data.get('id')
        user_name = user_data.get('name')
        print("[{}] {}".format(user_id,user_name))
    elif not response.json:
        print("No result")
    else:
        print("Not a valid JSON")

if __name__ =="__main__":
    if len(sys.argv)!= 2:
        sys.exit(1)
    elif len(sys.argv)== 1:
         q=""
    else:
        q = sys.argv[1]
    post_email(q)