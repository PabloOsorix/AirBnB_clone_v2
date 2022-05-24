#!/usr/bin/python3
"""
Script that starts a Flask web application
three routes (1.'/', 2.'/hbnb'). and new:
route 3: '/c/<text>
host: 0.0.0.0
port: 5000
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    string = text.replace('_', ' ')
    return "C {}".format(string)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
