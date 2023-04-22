from flask import Flask
from os import environ
app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hello_flask():
    """ Hbnb route """
    return "HBNB!"

if __name__ == '__main__':
    environ["FLASK_APP"] = __file__
    app.run(host='0.0.0.0', port=5000)

