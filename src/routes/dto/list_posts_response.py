from marshmallow import Schema, fields


class ListPostsUserResponse(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)

class ListPostsResponse(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    user = fields.Nested(ListPostsUserResponse, required=True)
