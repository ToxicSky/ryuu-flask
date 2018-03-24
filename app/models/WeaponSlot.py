from app import db


class WeaponSlot(db.Model):
    slot_id = db.Column(
        db.Integer,
        db.ForeignKey('slot.id'),
        primary_key=True,
        autoincrement=True
    )
    weapon_id = db.Column(
        db.Integer,
        db.ForeignKey('weapon.id'),
        primary_key=True
    )

    def __repr__(self):
        return '<Slot %r>' % self.label
