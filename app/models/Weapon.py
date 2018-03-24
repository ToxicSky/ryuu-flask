from app import db
from app.models.Mod import Mod
from app.models.WeaponProperty import WeaponProperty
from app.models.Slot import Slot
from app.library.utilities import typecast

weapon_slot = db.Table(
    'weapon_slot',
    db.Column('slot_id', db.Integer, db.ForeignKey(
        'slot.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
    db.Column('weapon_id', db.Integer, db.ForeignKey(
        'weapon.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
)


class Weapon(db.Model):
    __tablename__ = 'weapon'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(191), unique=True, nullable=False)
    properties = db.relationship(
        'WeaponProperty',
        # secondary=WeaponProperty,
        backref=db.backref('weapon', lazy=True, cascade='all, delete'),
        lazy='subquery'
    )
    slots = db.relationship(
        'Slot',
        secondary=weapon_slot,
        lazy='subquery',
        backref=db.backref('weapon', lazy=True, cascade='all, delete'),
        cascade="all, delete"
    )
    mods = db.relationship(
        'Mod',
        # secondary=Mod,
        lazy='subquery',
        backref=db.backref('mod', lazy=True),
        cascade="all, delete"
    )

    def flat_result(self):
        result = {'name': self.name}
        for weapon_property in self.properties:
            type_v = weapon_property.value_type
            key = weapon_property.property_key
            value = typecast(
                weapon_property.property_value, type_v)
            result[key] = value

        return result

    def __repr__(self):
        return '<Weapon - %r>' % self.name
