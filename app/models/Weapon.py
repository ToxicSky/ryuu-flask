from app import db
from app.models.Mod import Mod
from app.models.WeaponProperty import WeaponProperty
from app.models.Slot import Slot

weapon_slot = db.Table('weapon_slot',
                       db.Column('slot_id', db.Integer, db.ForeignKey(
                           'slot.id'), primary_key=True),
                       db.Column('weapon_id', db.Integer, db.ForeignKey(
                           'weapon.id'), primary_key=True)
                       )


class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(191), unique=True, nullable=False)
    properties = db.relationship(
        'WeaponProperty',
        backref='weapon_property',
        lazy=True
    )
    slots = db.relationship(
        'Slot',
        secondary=weapon_slot,
        lazy='subquery',
        backref=db.backref('weapon', lazy=True)
    )
    mods = db.relationship(
        'Mod',
        lazy='subquery',
        backref=db.backref('mod', lazy=True)
    )

    def flat_result(self):
        result = {'name': self.name}
        for weapon_property in self.properties:
            type_v = weapon_property.value_type
            key = weapon_property.property_key
            value = self.typecast(
                weapon_property.property_value, type_v)
            result[key] = value

        return result

    def typecast(self, value=None, type_v='str'):
        if (value == None):
            return

        if type_v == 'str':
            return str(value)
        if type_v == 'int':
            return int(value)
        if type_v == 'float':
            return float(value)
        if type_v == 'bool':
            return bool(value)

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Weapon - %r>' % self.name
