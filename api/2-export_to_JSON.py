"""imports"""

import json
import requests
import sys



def getInfo(id):
    """sending a request to url"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todourl = "{}/todos".format(url)

    request = requests.get(url)
    results = request.json()
    userid = results["id"]
    username = results["username"]

    request2 = requests.get(todourl)
    tasks = request2.json()

    alldata = {}

    jsondata = [
        {"task": task["title"], "completed": task["completed"], "username": username}
        for task in tasks
    ]

    alldata[str(userid)] = jsondata

    with open("{}.json".format(userid), "w") as jsonfile:
        json.dump(alldata, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
    else:
        id = 1
    getInfo(int(id))