from datetime import datetime


class UserModel:
    def __init__(self):
        self._users = [
            {
                'id': 1,
                'name': '홍길동',
                'email': 'hong@example.com',
                'created_at': datetime.now().isoformat()
            },
            {
                'id': 2,
                'name': '김철수',
                'email': 'kim@example.com',
                'created_at': datetime.now().isoformat()
            },
        ]
        self._next_id = 3

    def find_all(self):
        return self._users

    def find_by_id(self, user_id):
        for user in self._users:
            if user['id'] == user_id:
                return user
        return None

    def create(self, data):
        user = {
            'id': self._next_id,
            'name': data.get('name'),
            'email': data.get('email'),
            'created_at': datetime.now().isoformat()
        }
        self._next_id += 1
        self._users.append(user)
        return user

    def update(self, user_id, data):
        user = self.find_by_id(user_id)
        if not user:
            return None
        if 'name' in data:
            user['name'] = data['name']
        if 'email' in data:
            user['email'] = data['email']
        user['updated_at'] = datetime.now().isoformat()
        return user

    def remove(self, user_id):
        for i, user in enumerate(self._users):
            if user['id'] == user_id:
                self._users.pop(i)
                return True
        return False