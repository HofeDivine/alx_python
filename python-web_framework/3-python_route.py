"""
 a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000

"""
from flask import Flask
app = Flask(__name__)
@app.route('/',strict_slashes=False)
def hello():
    return 'Hello HBNB'
@app.route('/hbnb',strict_slashes=False)
def Hhello():
    return 'HBNB'
@app.route('/c/<text>',strict_slashes=False)
def displayC(text):
     return 'C {}'.format(text.replace('_', ' '))
@app.route('/python',strict_slashes=False)
@app.route('/python/<text>',strict_slashes=False)
def displayPy(text="is cool"):
    return 'Python {}'.format(text.replace('_', ' '))

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)