from flask import Blueprint, jsonify, request
from app.library.DamageResistanceCalc import DamageResistanceCalc
from app.library.InputValidator import InputValidator
calculators = Blueprint('calculators', __name__)
# Add prefix for api


@calculators.route('/api/calculators')
def index():
    options = {
        'damage_resistance': {
            'path': '/api/calculators/damage-resistance',
            'name': 'Damage Resistance'
        }
    }

    return jsonify(dict(options=options))


@calculators.route('/api/calculators/damage-resistance', methods=['post'])
def api_calc_damage_resistance():
    ###########################################################################
    # Returns how much damage either the enemy or the player makes
    # towards the other.
    # Paramaters used:
    #  - damage
    #  - damage_resist
    #  - difficulty
    #  - target (optional, default = player)
    ###########################################################################
    required = ['damage', 'damage_resist', 'difficulty']
    input_validator = InputValidator()
    valid = input_validator.validate(request.form, required)
    if not valid:
        errorMsg = 'Not all required values are present. You are missing %s.' % ', '.join(
            input_validator.missing
        )
        return jsonify({'error': errorMsg})

    damage = request.form['damage']
    damage_resist = request.form['damage_resist']

    dr = DamageResistanceCalc()
    if 'target' in request.form:
        dr.set_target(request.form['target'])
    dr.set_difficulty(request.form['difficulty'])
    result = dr.calc_coeff(damage, damage_resist)

    return jsonify(dict(damage_coeff=result))
