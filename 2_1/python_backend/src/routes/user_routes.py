from flask import Blueprint
from controllers.user_controller import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)

user_bp = Blueprint('users', __name__)

user_bp.route('/', methods=['GET'])(get_all_users)
user_bp.route('/<int:user_id>', methods=['GET'])(get_user_by_id)
user_bp.route('/', methods=['POST'])(create_user)
user_bp.route('/<int:user_id>', methods=['PUT'])(update_user)
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete_user)