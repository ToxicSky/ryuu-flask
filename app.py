#!/usr/bin/python
from flask import Flask, render_template
FalloutApp = Flask(__name__)


@FalloutApp.route("/")
def index():
    items = ['First', 'Second']
    return render_template('index.html', items=items)


@FalloutApp.route("/calculators")
def calculators():
    calc_list = [
        dict(link='damage-resistance', name='Damage Resistance')
    ]
    return render_template('calculators.html', calculators=calc_list)

if __name__ == "__main__":
    FalloutApp.run()
