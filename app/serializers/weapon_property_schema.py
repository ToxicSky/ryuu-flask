from app import ma
from app.models.WeaponProperty import WeaponProperty


class WeaponPropertySchema(ma.ModelSchema):
    class Meta:
        model = WeaponProperty
