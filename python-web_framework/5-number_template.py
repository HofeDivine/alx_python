import logging
from flask import Flask, render_template

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

@app.route('/', strict_slashes=False)
def hello():
    app.logger.info('Accessed / route')
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def Hhello():
    app.logger.info('Accessed /hbnb route')
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def displayC(text):
    app.logger.info('Accessed /c/{}'.format(text))
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
def displayPy(text="is cool"):
    app.logger.info('Accessed /python/{}'.format(text))
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def displayNumber(n):
    app.logger.info('Accessed /number/{}'.format(n))
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        return 'Not a valid integer'

@app.route('/number_template/<int:n>', strict_slashes=False)
def displayNumberTemplate(n):
    app.logger.info('Accessed /number_template/{}'.format(n))
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        return 'Not a valid integer'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

