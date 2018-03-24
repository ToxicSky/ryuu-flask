from app import db


class DamageResistanceSettings(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    difficulty = db.Column(db.Integer, db.ForeignKey('game_settings.id'))
    player_damage = db.Column(db.Float, nullable=False)
    enemy_damage = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<DamageResistanceSettings>'
