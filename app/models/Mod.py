from app import db
from app.models.ModProperty import ModProperty


class Mod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    weapon_id = db.Column(
        db.Integer,
        db.ForeignKey('weapon.id')
    )
    slot_id = db.Column(
        db.Integer,
        db.ForeignKey('slot.id')
    )
    properties = db.relationship(
        'ModProperty',
        backref='mod_property',
        lazy=True
    )

    slot = db.relationship(
        'Slot',
        backref='slot',
        lazy=True
    )

    def to_array(self):
        result = {'name': self.name, 'slot': self.slot.label}
        for prop in self.properties:
            value = self.typecast(prop.property_value, prop.value_type)
            result[prop.property_key] = value
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

    def __repr__(self):
        return '<Mod %r>' % self.name
