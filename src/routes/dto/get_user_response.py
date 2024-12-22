from marshmallow import Schema, fields


class GetUserResponse(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    created_at = fields.DateTime(required=True)