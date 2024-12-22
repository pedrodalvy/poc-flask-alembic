from http import HTTPStatus

from flask import Blueprint, request
from sqlalchemy.orm import joinedload

from src.models.base import db
from src.models.post import Post
from src.models.user import User
from src.routes.dto.create_post_response import CreatePostResponse
from src.routes.dto.get_post_response import GetPostResponse
from src.routes.dto.list_posts_response import ListPostsResponse
from src.routes.dto.update_post_response import UpdatePostResponse

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


@posts_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.options(joinedload(Post.user)).get_or_404(post_id)
    return GetPostResponse().dump(post)


@posts_bp.route('/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.options(joinedload(Post.user)).get_or_404(post_id)
    
    for key, value in request.json.items():
        setattr(post, key, value)
    
    db.session.commit()
    
    return UpdatePostResponse().dump(post)


@posts_bp.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    db.session.delete(post)
    db.session.commit()
    
    return '', HTTPStatus.NO_CONTENT
