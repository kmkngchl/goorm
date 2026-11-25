from flask import Blueprint
from controllers.chat_controller import (
    get_all_rooms,
    get_room,
    create_room,
    get_messages,
    send_message,
)

chat_bp = Blueprint('chats', __name__)

# 채팅방 관리
chat_bp.route('/', methods=['GET'])(get_all_rooms)
chat_bp.route('/', methods=['POST'])(create_room)
chat_bp.route('/<int:room_id>', methods=['GET'])(get_room)

# 메시지 관리
chat_bp.route('/<int:room_id>/messages', methods=['GET'])(get_messages)
chat_bp.route('/<int:room_id>/messages', methods=['POST'])(send_message)
