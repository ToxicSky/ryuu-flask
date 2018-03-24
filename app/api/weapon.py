from flask import Blueprint, jsonify, request
from app.models.Weapon import Weapon
from app.models.Slot import Slot
from app.models.WeaponProperty import WeaponProperty
from app.serializers.weapon_schema import WeaponSchema
from app.serializers.slot_schema import SlotSchema
from app.serializers.mod_schema import ModSchema
from app.serializers.weapon_property_schema import WeaponPropertySchema
from flask_jwt import jwt_required
from app import db
from app.library.utilities import get_one_or_create
weapon = Blueprint('weapon', __name__)


@weapon.route('/api/weapon')
def index():
    exclude_params = request.args.get('exclude', None)
    if exclude_params is not None:
        exclude = exclude_params.split(',')
    else:
        exclude = []

    only_params = request.args.get('only', None)
    if only_params is not None:
        only = only_params.split(',')
    else:
        only = []

    weapons = Weapon.query.all()
    weapon_schema = WeaponSchema(
        many=True,
        exclude=exclude,
        only=only
    )
    result = weapon_schema.dump(weapons)
    return jsonify(result.data)


@weapon.route('/api/weapon/<int:weapon_id>')
def find(weapon_id):
    weapons = Weapon.query.filter_by(id=weapon_id).first()
    weapon_schema = WeaponSchema()
    result = weapon_schema.dump(weapons)
    return jsonify(result.data)


@weapon.route('/api/weapon/search')
def search():
    params = request.args
    search_query = []
    for key in params:
        like = getattr(Weapon, key).like('%' + params[key] + '%')
        search_query.append(like)
    weapon = Weapon.query.filter(*search_query).all()
    weapon_schema = WeaponSchema(many=True)
    return jsonify(weapon_schema.dump(weapon).data)


@weapon.route('/api/weapon', methods=['POST'])
@jwt_required()
def post():
    weapon_data = request.json.get('weapon', None)
    mods_data = request.json.get('mods', None)
    properties_data = request.json.get('properties', None)
    slots_data = request.json.get('slots', None)

    weapon = get_one_or_create(Weapon, weapon_data)

    db.session.add(weapon)
    if slots_data is not None:
        for slot in slots_data:
            slot_db = get_one_or_create(Slot, slot)
            weapon.slots.append(slot_db)

    if properties_data is not None:
        for weapon_property in properties_data:
            property_db = get_one_or_create(WeaponProperty, weapon_property)
            weapon.properties.append(property_db)

    if mods_data is not None:
        for mod in mods_data:
            mod_db = get_one_or_create(Mod, mod)
            weapon.mods.append(mod_db)

    db.session.commit()

    weapon_schema = WeaponSchema()
    weapon = weapon_schema.dump(weapon).data

    return jsonify(weapon)


@weapon.route('/api/weapon/<int:weapon_id>', methods=['PUT'])
@jwt_required()
def put(weapon_id):
    weapon = Weapon.query.filter_by(id=weapon_id).first()
    if weapon is None:
        return jsonify({'error': 'No weapon by id %r was found.' % weapon_id})

    add = request.json.get('add', {})
    remove = request.json.get('remove', {})

    mods_add = add.get('mods', [])
    mods_remove = remove.get('mods', [])

    properties_add = add.get('properties', [])
    properties_remove = remove.get('properties', [])

    slots_add = add.get('slots', [])
    slots_remove = remove.get('slots', [])

    for slot in slots_remove:
        slot_db = get_one_or_create(Slot, slot)
        weapon.slots.remove(slot_db)

    for slot in slots_add:
        slot_db = get_one_or_create(Slot, slot)
        weapon.slots.append(slot_db)

    for weapon_property in properties_remove:
        property_db = get_one_or_create(WeaponProperty, weapon_property)
        weapon.propertys.remove(property_db)

    for weapon_property in properties_add:
        property_db = get_one_or_create(WeaponProperty, weapon_property)
        weapon.properties.append(property_db)

    for mod in mods_add:
        mod_db = get_one_or_create(Mod, mod)
        weapon.mods.append(mod_db)
    db.session.commit()
    weapon_schema = WeaponSchema()
    return jsonify(weapon_schema.dump(weapon).data)


@weapon.route('/api/weapon/<int:weapon_id>', methods=['DELETE'])
@jwt_required()
def delete(weapon_id):
    deleted = Weapon.query.filter_by(id=weapon_id).delete()
    db.session.commit()
    if deleted:
        message = {'message': 'Weapon wass successfully deleted.'}
    else:
        message = {'error': 'Failed to delete weapon.'}
    return jsonify(message)
