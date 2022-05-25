#!/usr/bin/python3
"""
Script that starts a Flask web application
it use storafe from  the storage engine.
It have 2 routes
(1.route: /states)
(2.route: /states/<id>)
"""

from logging import exception
from xml.dom import NotFoundErr
from models.state import State
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_cities_list():
    """Display a list of all States in the DB
    """
    state_list = storage.all(State)
    return render_template('9-states.html', html_list=state_list)

@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Display the cities of a state if
    a object State is found with this id"""
    states_list = storage.all(State)
    id = id
    switch = 1
    state = None
    state = states_list.get("State.{}".format(id))
    if state is not None:
        switch = 0
    return render_template('9-states.html', html_state=state, id=switch)


@app.teardown_appcontext
def close(exception):
    """Close currently session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
