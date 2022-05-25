#!/usr/bin/python3
"""
Script that starts a Flask web application
it use storafe from  the storage engine.
It have 4 routes
(1.route: /states_list)
(2. route: H1 tag states)
(3. route: UL taf list all states)
(4. route: LI taf description of one state)
"""

from models import State
from models import storage
from models import City
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    state_list = {}
    state_list = storage.all(State).copy()
    return render_template('8-cities_by_states.html', html_list=state_list)


@app.teardown_appcontext
def close(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
