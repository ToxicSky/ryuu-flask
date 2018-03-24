from app import ma
from marshmallow import Schema, fields, post_load
from app.models.Slot import Slot


class SlotSchema(ma.ModelSchema):
    label = fields.Str()
    category = fields.Str()

    class Meta:
        model = Slot
