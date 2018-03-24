from app import db


class GameSettings(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    setting_key = db.Column(db.String(191), unique=True, nullable=False)
    setting_value = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return '<GameSettings %r>' % self.setting_key
