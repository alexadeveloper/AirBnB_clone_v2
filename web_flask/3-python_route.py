#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask

aplication = Flask(__name__)


@aplication.route('/', strict_slashes=False)
def hello():
    """ Displays hello message """
    return "Hello HBNB!"


@aplication.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays hello message """
    return "HBNB"


@aplication.route('/c/<text>', strict_slashes=False)
def croute(text):
    """ Displays hello message """
    return "C %s" % text.replace('_', ' ')


@aplication.route('/python/', defaults={'text': 'is_cool'})
@aplication.route('/python/<text>', strict_slashes=False)
def pythonroute(text='is_cool'):
    """ Displays hello message """
    return "Python %s" % text.replace('_', ' ')
if __name__ == '__main__':
    aplication.run(host='0.0.0.0')
