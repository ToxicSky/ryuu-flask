from app import db

# Check up how to best describe location. (Zone)


class LocationAttribute(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    parent = db.Column(
        db.Integer,
        db.ForeignKey('location_attribute.id',
                      onupdate='CASCADE', ondelete='CASCADE'),
        nullable=True
    )
    location = db.Column(
        db.Integer,
        db.ForeignKey('location.id')
    )
    zone = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Mod %r>' % self.name
