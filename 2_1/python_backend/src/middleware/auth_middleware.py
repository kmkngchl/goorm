from functools import wraps
from flask import request, jsonify
import jwt
import os


def authenticate_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return jsonify({'success': False, 'message': '인증 토큰이 필요합니다.'}), 401
        token = parts[1]
        try:
            jwt.decode(
                token,
                os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production'),
                algorithms=['HS256']
            )
        except Exception:
            return jsonify({'success': False, 'message': '유효하지 않은 토큰입니다.'}), 403
        return f(*args, **kwargs)
    return decorated