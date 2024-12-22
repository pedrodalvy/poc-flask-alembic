from marshmallow import Schema, fields


class CreatePostResponse(Schema):
    id = fields.Int(required=True)
