#!/usr/bin/python3
""" Starts a flash web application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def numb(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def numbtemp(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    x = "even" if n % 2 == 0 else "odd"
    return render_template(
        '6-number_odd_or_even.html', n=n, x=x


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
