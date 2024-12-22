from http import HTTPStatus

from flask import Blueprint, request
from sqlalchemy.orm import joinedload

from src.models.base import db
from src.models.post import Post
from src.models.user import User
from src.routes.dto.create_post_response import CreatePostResponse
from src.routes.dto.list_posts_response import ListPostsResponse

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('/', methods=['GET'])
def posts_list():
    posts = Post.query.options(joinedload(Post.user)).all()
    return ListPostsResponse(many=True).dump(posts)


@posts_bp.route('/', methods=['POST'])
def create_post():
    post = Post(**request.json)
    user = User.query.get_or_404(post.created_by)
    post.user = user

    db.session.add(post)
    db.session.commit()

    return CreatePostResponse().dump(post), HTTPStatus.CREATED
