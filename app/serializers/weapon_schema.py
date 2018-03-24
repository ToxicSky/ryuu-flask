from app import ma
from app.models.Weapon import Weapon
from app.serializers.mod_schema import ModSchema
from app.serializers.slot_schema import SlotSchema
from app.serializers.weapon_property_schema import WeaponPropertySchema
from marshmallow import Schema, fields, post_load


class WeaponSchema(ma.ModelSchema):
    name = fields.Str()

    class Meta:
        model = Weapon

    mods = ma.Nested(ModSchema, many=True)
    slots = ma.Nested(SlotSchema, many=True)
    properties = ma.Nested(WeaponPropertySchema, many=True)

    @post_load
    def make_weapon(self, weapon):
        return weapon
