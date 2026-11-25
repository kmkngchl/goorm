from flask import jsonify, request
from models.chat_model import ChatModel

chat_model = ChatModel()


def get_all_rooms():
    """채팅방 목록 조회"""
    rooms = chat_model.get_all_rooms()
    return jsonify({'success': True, 'data': rooms})


def get_room(room_id):
    """채팅방 상세 조회"""
    room = chat_model.get_room_by_id(room_id)
    if not room:
        return jsonify({'success': False, 'message': '채팅방을 찾을 수 없습니다.'}), 404
    return jsonify({'success': True, 'data': room})


def create_room():
    """채팅방 생성"""
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'success': False, 'message': '방 이름은 필수입니다.'}), 400
    new_room = chat_model.create_room(data['name'])
    return jsonify({'success': True, 'data': new_room}), 201


def get_messages(room_id):
    """특정 채팅방의 메시지 목록 조회"""
    room = chat_model.get_room_by_id(room_id)
    if not room:
        return jsonify({'success': False, 'message': '채팅방을 찾을 수 없습니다.'}), 404
    messages = chat_model.get_messages(room_id)
    return jsonify({'success': True, 'data': messages})


def send_message(room_id):
    """메시지 전송"""
    room = chat_model.get_room_by_id(room_id)
    if not room:
        return jsonify({'success': False, 'message': '채팅방을 찾을 수 없습니다.'}), 404

    data = request.get_json()
    if not data or not data.get('content'):
        return jsonify({'success': False, 'message': '메시지 내용은 필수입니다.'}), 400

    user_id = data.get('user_id', 0)
    user_name = data.get('user_name', '익명')
    content = data['content']

    new_message = chat_model.add_message(room_id, user_id, user_name, content)
    return jsonify({'success': True, 'data': new_message}), 201