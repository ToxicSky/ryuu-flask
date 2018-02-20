from app import db


class Slot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(191), unique=True, nullable=False)
    category = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Slot %r>' % self.label
