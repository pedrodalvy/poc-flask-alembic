from flask import Blueprint, request, Response

from src.models.base import db
from src.models.user import User
from src.routes.dto.create_user_response import CreateUserResponse
from src.routes.dto.get_user_response import GetUserResponse
from src.routes.dto.list_users_response import ListUsersResponse

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=['GET'])
def users_list() -> Response:
    users =  User.query.all()
    return ListUsersResponse(many=True).dump(users)


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int) -> Response:
    user = User.query.get_or_404(user_id)
    return GetUserResponse().dump(user)


@users_bp.route('/', methods=['POST'])
def create_user() -> Response:
    user = User(**request.json)
    db.session.add(user)
    db.session.commit()

    return CreateUserResponse().dump(user)
