#!/usr/bin/python3
"""
Scriot that starts a Flask web application
It have four routes
(1. route: '/') (2. route: '/hbnb')
(3. route: /c/<text>) and (4./python/<text>)
host: 0.0.0.0
port: 5000
"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
