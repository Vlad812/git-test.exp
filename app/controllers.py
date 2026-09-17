from flask import Blueprint, request, jsonify
from app.models import db, Article

articles_bp = Blueprint('articles', __name__, url_prefix='/api/articles')


@articles_bp.route('', methods=['GET'])
def get_all_articles():
    """Получить все статьи"""
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return jsonify({
        'success': True,
        'data': [article.to_dict() for article in articles]
    }), 200


@articles_bp.route('/<int:article_id>', methods=['GET'])
def get_article(article_id):
    """Получить одну статью по ID"""
    article = Article.query.get_or_404(article_id)
    return jsonify({
        'success': True,
        'data': article.to_dict()
    }), 200


@articles_bp.route('', methods=['POST'])
def create_article():
    """Создать новую статью"""
    data = request.get_json()

    if not data:
        return jsonify({
            'success': False,
            'error': 'No data provided'
        }), 400

    required_fields = ['title', 'content']
    missing_fields = [field for field in required_fields if not data.get(field)]

    if missing_fields:
        return jsonify({
            'success': False,
            'error': f'Missing required fields: {", ".join(missing_fields)}'
        }), 400

    article = Article(
        title=data['title'],
        content=data['content'],
        author=data.get('author', 'Anonymous')
    )

    db.session.add(article)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Article created successfully',
        'data': article.to_dict()
    }), 201


@articles_bp.route('/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    """Обновить существующую статью"""
    article = Article.query.get_or_404(article_id)
    data = request.get_json()

    if not data:
        return jsonify({
            'success': False,
            'error': 'No data provided'
        }), 400

    # Обновляем только переданные поля
    if 'title' in data:
        article.title = data['title']
    if 'content' in data:
        article.content = data['content']
    if 'author' in data:
        article.author = data['author']

    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Article updated successfully',
        'data': article.to_dict()
    }), 200


@articles_bp.route('/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    """Удалить статью"""
    article = Article.query.get_or_404(article_id)

    db.session.delete(article)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Article deleted successfully'
    }), 200
