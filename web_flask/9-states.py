#!/usr/bin/python3
"""Start a Flask web application"""


from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """close function"""
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def states(id=None):
    """function to execute"""
    states = storage.all(State)
    state_id = None
    state = None

if id:
    state_id = 'State.' + id
    if state_id in states.keys():
        state = states[state_id]
    return render_template('9-states.html', state=state,
                           id=state_id, states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
