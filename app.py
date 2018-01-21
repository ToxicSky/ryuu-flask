#!/usr/bin/python
from flask import Flask, render_template
FalloutApp = Flask(__name__)


@FalloutApp.route("/")
def index():
    items = ['First', 'Second']
    return render_template('index.html', items=items)

if __name__ == "__main__":
    FalloutApp.run()
