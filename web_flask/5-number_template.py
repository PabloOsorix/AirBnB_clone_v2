#!/usr/bin/python3
"""
Scriot that starts a Flask web application
It have five routes/
(1. route: '/') (2. route: '/hbnb')
(3. route: /c/<text>) and (4./python/<text>)
(5. route: /number/<n>)
host: 0.0.0.0
port: 5000
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    string = text.replace('_', ' ')
    return 'C {}'.format(string)


@app.route('/python',  strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    string = text.replace('_', ' ')
    return 'Python {}'.format(string)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', Number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
