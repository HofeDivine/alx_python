
"""
 a new script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def Hhello():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def displayC(text):
    return 'C {}'.format(text.replace('_', ' '))
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def displayPy(text="is cool"):
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def displayNumber(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def displayNumberTemplate(n):
    
    return render_template('templates/5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
