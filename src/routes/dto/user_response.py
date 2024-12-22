from marshmallow import Schema, fields


class UserResponse(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
