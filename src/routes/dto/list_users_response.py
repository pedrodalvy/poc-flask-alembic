from marshmallow import Schema, fields


class ListUsersResponse(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
