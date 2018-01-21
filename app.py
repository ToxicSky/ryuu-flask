#!/usr/bin/python
from flask import Flask, render_template
FalloutApp = Flask(__name__)

@FalloutApp.route("/")
def index():
	return 'Hello, Flask!'

@FalloutApp.route("/hello")
def hello():
	return "Hello!"

if __name__ == "__main__":
	FalloutApp.run()
