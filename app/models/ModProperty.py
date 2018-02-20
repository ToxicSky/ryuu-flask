from app import db


class ModProperty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_key = db.Column(db.String(255), nullable=False)
    property_value = db.Column(db.String(255), nullable=False)
    value_type = db.Column(db.String(255), nullable=False, default='str')
    mod_id = db.Column(
        db.Integer,
        db.ForeignKey('mod.id')
    )

    # def __init__(self, id, property_key, property_value):
    #     self.property_key = property_key
    #     self.property_value = property_value

    def __repr__(self):
        return '<ModProperty %r>' % self.property_key
