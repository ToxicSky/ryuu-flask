from app import db


class WeaponProperty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('weapon.id'))
    property_key = db.Column(db.String(255), unique=False, nullable=False)
    property_value = db.Column(db.String(255), unique=False, nullable=False)
    value_type = db.Column(db.String(255), nullable=False, default='str')

    def __init(self, id, item_id, property_key, property_value, value_type):
        self.id = id
        self.item_id = item_id
        self.property_key = property_key
        self.property_value = property_value
        self.value_type = value_type

    def __repr__(self):
        return '<WeaponProperty %r>' % self.property_key
