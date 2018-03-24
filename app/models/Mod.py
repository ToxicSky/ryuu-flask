from app import db
from app.models.ModProperty import ModProperty
from app.library.utilities import typecast


class Mod(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(255), nullable=False)
    weapon_id = db.Column(
        db.Integer,
        db.ForeignKey('weapon.id', onupdate='CASCADE', ondelete='CASCADE')
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
            value = typecast(prop.property_value, prop.value_type)
            result[prop.property_key] = value
        return result

    def __repr__(self):
        return '<Mod %r>' % self.name
