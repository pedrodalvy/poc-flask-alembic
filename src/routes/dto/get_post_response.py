from marshmallow import Schema, fields

from src.routes.dto.user_response import UserResponse


class GetPostResponse(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    created_by = fields.Int(required=True)
    user = fields.Nested(UserResponse, required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
