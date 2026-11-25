from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'success': False, 'message': '요청한 리소스를 찾을 수 없습니다.'}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({'success': False, 'message': '서버 내부 오류가 발생했습니다.'}), 500