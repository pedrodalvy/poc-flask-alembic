from marshmallow import Schema, fields


class CreateUserResponse(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
