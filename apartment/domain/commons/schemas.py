from marshmallow import fields, Schema

class LocationSchema(Schema):
    lat = fields.Float(required=True)
    lng = fields.Float(required=True)

class PlaceSchema(Schema):
    address = fields.String(required=True)
    location = fields.Nested(LocationSchema, required=True)
