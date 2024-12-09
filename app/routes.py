from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .models import Book, Category, db
from .test import test

main = Blueprint('main', __name__)

@main.route('/library', methods=['GET'])
@login_required
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        output.append({
            'title': book.title,
            'autor': book.autor,
            'category': book.category,
            'status': book.status
        })
    return jsonify(output)

@main.route('/library', methods=['POST'])
@login_required
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        autor=data['autor'],
        category=data['category'],
        status=data.get('status', 'shelf')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added!'}), 201

@main.route('/categories', methods=['POST'])
@login_required
def add_category():
    data = request.get_json()
    new_category = Category(name=data['name'], user_id=current_user.id)
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category added!'}), 201

@main.route('/test', methods = ['GET'])
def run_test():
    test()
    return jsonify({'message': 'Test executed!'}), 201
