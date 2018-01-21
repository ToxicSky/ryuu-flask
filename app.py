#!/usr/bin/python
from flask import Flask, render_template
FalloutApp = Flask(__name__)


@FalloutApp.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    FalloutApp.run()
