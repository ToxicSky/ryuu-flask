from flask import Blueprint, jsonify, request
from app.library.WeaponAssembler import WeaponAssembler
from app.models.Weapon import Weapon
from app.models.Mod import Mod

weapon_assembler = Blueprint('weapon_assembler', __name__)


@weapon_assembler.route('/api/assemble/weapon')
def index():
    weapon_id = request.args.get('weapon', None)
    mods_id = request.args.get('mods', None)

    if mods_id is not None:
        mods = Mod.query.filter(Mod.id.in_(mods_id.split(','))).all()
    else:
        mods = []

    wa = WeaponAssembler()

    weapon = Weapon.query.filter_by(id=weapon_id).first()
    wa.set_weapon(weapon.flat_result())
    for slot in weapon.slots:
        wa.add_slot(slot.label)

    for mod in mods:
        wa.add_mod(mod.to_array())

    result = wa.assemble()
    return jsonify(result)
