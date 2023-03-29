#!/usr/bin/python3
""" starts flask app """

from flask import Flask, render_template
from models import storage, state

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    states = storage.all(state.State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(states_list):
    """Call close"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
