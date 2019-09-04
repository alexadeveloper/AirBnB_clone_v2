#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask

aplication = Flask(__name__)


@aplication.route('/', strict_slashes=False)
def hello():
    """ Displays hello message """
    return "Hello HBNB!"


@aplication.route('/', strict_slashes=False)
def hbnb():
    """ Displays hello message """
    return "HBNB"


if __name__ == '__main__':
    aplication.run(host='0.0.0.0')
