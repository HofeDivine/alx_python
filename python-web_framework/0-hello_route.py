"""
A script   that starts a Flask web application:
listening on host 0.0.0.0 and port 5000
"""
from flask import Flask
app = Flask(__name__)
@app.route('/',strict_slashes=False)
def hello():
    """
    A function that returns a string on the homepage of a web application
    """
    return "Hello HBNB!"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
    