from app import db


class ModProperty(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    property_key = db.Column(db.String(255), nullable=False)
    property_value = db.Column(db.String(255), nullable=False)
    value_type = db.Column(db.String(255), nullable=False, default='str')
    mod_id = db.Column(
        db.Integer,
        db.ForeignKey('mod.id', onupdate='CASCADE', ondelete='CASCADE')
    )

    def __repr__(self):
        return '<ModProperty %r>' % self.property_key
