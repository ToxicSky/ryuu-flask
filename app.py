#!/usr/bin/python
from flask import Flask, render_template, request, jsonify
from library.DamageResistanceCalc import DamangeResistanceCalc

FalloutApp = Flask(__name__)


@FalloutApp.route('/', methods=['GET'])
def index():
    items = ['First', 'Second']
    return render_template('index.html', items=items)


@FalloutApp.route('/calculators', methods=['GET'])
def calculators():
    calc_list = [
        dict(link='/calculators/damage-resistance', name='Damage Resistance')
    ]
    return render_template('calculators.html', calculators=calc_list)


@FalloutApp.route('/calculators/damage-resistance', methods=['GET'])
def calc_damage_resistance():
    return render_template(
        'calculators/damage_resistance.html', damage_coeff=0
    )


@FalloutApp.route('/api/calculators/damage-resistance', methods=['POST'])
def api_calc_damage_resistance():
    damage = request.form['damage']
    damage_resist = request.form['damage_resist']

    dr = DamangeResistanceCalc()
    result = dr.damage_coeff(damage, damage_resist)
    return jsonify(dict(damage_coeff=result))

if __name__ == '__main__':
    FalloutApp.run()
