from app import ma
from app.models.Enemy import Enemy


class EnemySchema(ma.ModelSchema):
    class Meta:
        model = Enemy
