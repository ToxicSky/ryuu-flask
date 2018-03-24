from app import ma
from app.models.Mod import Mod
from app.serializers.slot_schema import SlotSchema
from app.serializers.mod_property_schema import ModPropertySchema


class ModSchema(ma.ModelSchema):
    class Meta:
        model = Mod

    slot = ma.Nested(SlotSchema)
    properties = ma.Nested(ModPropertySchema, many=True)
