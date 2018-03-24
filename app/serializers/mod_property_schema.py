from app import ma
from app.models.ModProperty import ModProperty


class ModPropertySchema(ma.ModelSchema):
    class Meta:
        model = ModProperty
