import logging

from flask import Blueprint, jsonify
from werkzeug.exceptions import abort

from bp_posts.dao.post import Post
from bp_posts.views import post_dao

blueprint_api = Blueprint("api", __name__)

api_logger = logging.getLogger("api_logger")


@blueprint_api.route('/')
def help_endpoints():
    return "Эндпоинты: /posts и /posts/'post_id'"


@blueprint_api.route('/posts/')
def api_posts():
    """Endpoints for all posts"""
    posts: list[Post] = post_dao.get_all()
    api_logger.debug("Загрузка всех постов")

    return jsonify([post.as_dict() for post in posts]), 200


@blueprint_api.route('/posts/<int:pk>')
def api_post_id(pk):
    """Endpoint for one post"""
    post: Post | None = post_dao.get_by_pk(pk)
    if post is None:
        api_logger.debug(f"Обращение к несуществующему посту {pk}")
        abort(404)

    api_logger.debug(f"Загрузка поста {pk}")
    return jsonify(post.as_dict()), 200


@blueprint_api.errorhandler(404)
def api_error_404(e):
    api_logger.error(f"Ошибка {e}")
    return jsonify({'message': str(e)}), 404
