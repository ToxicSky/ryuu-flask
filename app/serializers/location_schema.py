from app import ma
from app.models.Location import Location, LocationAttribute, LocationNotable


class LocationAttributeSchema(ma.ModelSchema):
    class Meta:
        model = LocationAttribute


class LocationNotableSchema(ma.ModelSchema):
    class Meta:
        model = LocationNotable


class LocationSchema(ma.ModelSchema):
    class Meta:
        model = Location

    attributes = ma.Nested(LocationAttributeSchema, many=True)
    notables = ma.Nested(LocationNotableSchema, many=True)
