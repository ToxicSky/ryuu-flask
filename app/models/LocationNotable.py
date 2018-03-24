from app import db

# notable_type, change to enum
# reference, add enemies to trial


class LocationNotable(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    location = db.Column(
        db.Integer,
        db.ForeignKey('location.id', onupdate='CASCADE', ondelete='CASCADE')
    )
    name = db.Column(db.String(255), nullable=False)
    notable_type = db.Column(db.String(255), nullable=False)
    reference = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<LocationNotable %r>' % self.name
