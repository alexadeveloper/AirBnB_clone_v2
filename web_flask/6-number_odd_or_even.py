#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
from flask import render_template
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


@aplication.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Displays hello message """
    return "%d is a number" % n


@aplication.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays hello message """
    return render_template('5-number.html', n=n)


@aplication.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ Displays hello message """
    return render_template('6-number_odd_or_even.html', n=n)
if __name__ == '__main__':
    aplication.run(host='0.0.0.0')
