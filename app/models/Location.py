from app import db
# Look into making a map-api, similar to Google Maps, but for Fallout.


class Location(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(191), unique=True, nullable=False)
    attributes = db.relationship(
        'LocationAttribute',
        backref='location_attribute',
        lazy=True
    )
    notables = db.relationship(
        'LocationNotable',
        backref='location_notable',
        lazy=True
    )

    def __repr__(self):
        return '<Location %r>' % self.name


class LocationNotable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(
        db.Integer,
        db.ForeignKey('location.id')
    )
    name = db.Column(db.String(255), nullable=False)
    notable_type = db.Column(db.String(255), nullable=False)
    reference = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<LocationNotable %r>' % self.name


class LocationAttribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent = db.Column(
        db.Integer,
        db.ForeignKey('location_attribute.id'),
        nullable=True
    )
    location = db.Column(
        db.Integer,
        db.ForeignKey('location.id')
    )
    zone = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<LocationAttribute %r>' % self.zone
