#!/usr/bin/python3
"""
Script that starts a Flask web application
it use storafe from  the storage engine.
It have 1 route
(1.route: /cities_by_states)
"""


from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_cities_list():
    """Display a list of states and cities
    """
    state_list = storage.all("State")
    return render_template('8-cities_by_states.html', html_list=state_list)


@app.teardown_appcontext
def close(exception):
    """Close currently session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
