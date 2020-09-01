#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def message_1():
    """return a message"""

    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def message_2():
    """return a message"""

    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def message_3(text):
    """return a message"""
    text = text.replace('_', ' ')
    return ("C {}".format(text))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def message_4(text="is cool"):
    """return a message"""
    text = text.replace('_', ' ')
    return ("Python {}".format(text))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')