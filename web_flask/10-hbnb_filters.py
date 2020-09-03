#!/usr/bin/python3
"""Starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Close function"""

    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def function_filters(id=None):
    """connect with filters temp"""

    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        '10-hbnb_filters.html', states, amenities)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
