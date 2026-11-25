from flask import jsonify, request
from models.user_model import UserModel

user_model = UserModel()


def get_all_users():
    """사용자 목록 조회"""
    users = user_model.find_all()
    return jsonify({'success': True, 'data': users})


def get_user_by_id(user_id):
    """사용자 상세 조회"""
    user = user_model.find_by_id(user_id)
    if not user:
        return jsonify({'success': False, 'message': '사용자를 찾을 수 없습니다.'}), 404
    return jsonify({'success': True, 'data': user})


def create_user():
    """사용자 생성"""
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({'success': False, 'message': '이름과 이메일은 필수입니다.'}), 400
    new_user = user_model.create(data)
    return jsonify({'success': True, 'data': new_user}), 201


def update_user(user_id):
    """사용자 수정"""
    data = request.get_json()
    updated_user = user_model.update(user_id, data)
    if not updated_user:
        return jsonify({'success': False, 'message': '사용자를 찾을 수 없습니다.'}), 404
    return jsonify({'success': True, 'data': updated_user})


def delete_user(user_id):
    """사용자 삭제"""
    deleted = user_model.remove(user_id)
    if not deleted:
        return jsonify({'success': False, 'message': '사용자를 찾을 수 없습니다.'}), 404
    return jsonify({'success': True, 'message': '사용자가 삭제되었습니다.'})