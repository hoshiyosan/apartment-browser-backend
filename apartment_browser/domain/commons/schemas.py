"""
Defines commons schemas that can be re-used accross other schemas.
"""
from marshmallow import fields, Schema


class LocationSchema(Schema):
    """
    Schema used to validate gps coordinates.
    """
    lat = fields.Float(required=True)
    lng = fields.Float(required=True)


class PlaceSchema(Schema):
    """
    Schema used to validate place object.
    """
    address = fields.String(required=True)
    location = fields.Nested(LocationSchema, required=True)
