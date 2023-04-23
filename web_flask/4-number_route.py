
#!/usr/bin/python3
"""Flask Module"""

from flask import Flask
from os import environ
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Entry route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_flask():
    """ Hbnb route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ c is fun(:\) route """
    textreplace = text.replace('_',' ')
    return "C {}".format(textreplace)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text='is cool'):
    """ python is cool route """
    textreplace = text.replace('_',' ')
    return "Python {}".format(textreplace)


@app.route('/number/<int:n>', strict_slashes=False)
def route_int(n):
    """ integer route """
    return "{} is a number".format(n)


if __name__ == '__main__':
    environ["FLASK_APP"] = __file__
    app.run(host='0.0.0.0', port=5000)
