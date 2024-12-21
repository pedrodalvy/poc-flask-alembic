from marshmallow import Schema, fields


class CreateUserResponse(Schema):
    id = fields.Int(required=True)
