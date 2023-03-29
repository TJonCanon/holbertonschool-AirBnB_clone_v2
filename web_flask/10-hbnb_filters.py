#!/usr/bin/python3
""" starts flask app """
from flask import Flask, render_template
from models import storage, state, amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters():
    return render_template("10-hbnb_filters.html",
                           states=storage.all(state.State),
                           amenities=storage.all(amenity.Amenity))


@app.teardown_appcontext
def teardown(something):
    """ close """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
