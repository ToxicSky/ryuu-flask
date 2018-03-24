from app import db

# notable_type, change to enum
# reference, add enemies to trial


class EnemyBase(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(db.String(191), unique=True, nullable=False)
    variations = db.relationship(
        'Enemy',
        backref='enemy',
        lazy=True
    )

    def __repr__(self):
        return '<Enemy %r>' % self.name


class Enemy(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    base_id = db.Column(
        db.Integer,
        db.ForeignKey('enemy_base.id', onupdate='CASCADE', ondelete='CASCADE')
    )
    name = db.Column(db.String(191), unique=True, nullable=False)
    attributes = db.relationship(
        'EnemyAttribute',
        backref='enemy_attribute',
        lazy=True
    )


class EnemyAttribute(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    enemy_id = db.Column(
        db.Integer,
        db.ForeignKey('enemy.id', onupdate='CASCADE', ondelete='CASCADE')
    )
    attribute_key = db.Column(db.String(255), nullable=False)
    attribute_value = db.Column(db.String(255), nullable=False)
    attribute_type = db.Column(db.String(255), nullable=False)
