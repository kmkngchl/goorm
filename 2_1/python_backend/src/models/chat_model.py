from datetime import datetime


class ChatModel:
    def __init__(self):
        self._rooms = [
            {
                'id': 1,
                'name': '일반 대화방',
                'created_at': datetime.now().isoformat()
            },
            {
                'id': 2,
                'name': '개발자 수다방',
                'created_at': datetime.now().isoformat()
            },
        ]
        self._next_room_id = 3
        self._messages = [
            {
                'id': 1,
                'room_id': 1,
                'user_id': 1,
                'user_name': '홍길동',
                'content': '안녕하세요! 채팅방에 오신 것을 환영합니다.',
                'created_at': datetime.now().isoformat()
            },
        ]
        self._next_message_id = 2

    # --- 방 관리 ---
    def get_all_rooms(self):
        return self._rooms

    def get_room_by_id(self, room_id):
        for room in self._rooms:
            if room['id'] == room_id:
                return room
        return None

    def create_room(self, name):
        room = {
            'id': self._next_room_id,
            'name': name,
            'created_at': datetime.now().isoformat()
        }
        self._next_room_id += 1
        self._rooms.append(room)
        return room

    # --- 메시지 관리 ---
    def get_messages(self, room_id):
        return [m for m in self._messages if m['room_id'] == room_id]

    def add_message(self, room_id, user_id, user_name, content):
        message = {
            'id': self._next_message_id,
            'room_id': room_id,
            'user_id': user_id,
            'user_name': user_name,
            'content': content,
            'created_at': datetime.now().isoformat()
        }
        self._next_message_id += 1
        self._messages.append(message)
        return message