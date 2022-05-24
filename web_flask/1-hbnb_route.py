#!/usr/bin/python3
"""
Script that starts a Flask web application,
it have two functions to two routes
route 1: '/'
route 2: '/hbnb'
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
