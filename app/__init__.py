import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify
from app.models import db
from app.controllers import articles_bp


def create_app():
    """Функция создания и настройки приложения Flask"""
    app = Flask(__name__)

    # Конфигурация базы данных (SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'

    # Инициализация базы данных
    db.init_app(app)

    # Регистрация blueprint для статей
    app.register_blueprint(articles_bp)

    # Создание таблиц базы данных
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        """Главная страница с информацией о API"""
        return jsonify({
            'message': 'Articles CRUD API',
            'endpoints': {
                'GET /api/articles': 'Получить все статьи',
                'GET /api/articles/<id>': 'Получить статью по ID',
                'POST /api/articles': 'Создать новую статью',
                'PUT /api/articles/<id>': 'Обновить статью',
                'DELETE /api/articles/<id>': 'Удалить статью'
            }
        }), 200

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 'Not found'
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'error': 'Internal server error'
        }), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
