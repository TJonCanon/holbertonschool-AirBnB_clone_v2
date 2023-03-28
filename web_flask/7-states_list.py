#!/usr/bin/python3
""" starts flask app """

from flask import Flask, render_template
from models import storage
from models.state import State


app = flask(__name__)


@app.route('/states_list', strict_slashes=False)
def statelist():
    return render_template("7-states_list.html", db=storage.all(State))


@app.teardown_appcontext
def methd(content):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
