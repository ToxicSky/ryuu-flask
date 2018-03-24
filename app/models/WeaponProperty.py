from app import db
# from app.models.Weapon import Weapon


class WeaponProperty(db.Model):
    __tablename__ = 'weapon_property'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(
        db.Integer,
        db.ForeignKey('weapon.id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True
    )
    property_key = db.Column(db.String(255), unique=False, nullable=False)
    property_value = db.Column(db.String(255), unique=False, nullable=False)
    value_type = db.Column(db.String(255), nullable=False, default='str')

    def __repr__(self):
        return '<WeaponProperty %r>' % self.property_key
