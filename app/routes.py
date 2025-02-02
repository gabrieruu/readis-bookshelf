from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from .models import ReadListStatus, BuyListStatus, Book, Category, db
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
            'author': book.author,
            'read_list_status': book.read_list_status.value,
            'buy_list_status': book.buy_list_status.value,
            'user_id': book.user_id
        })
    return jsonify(output), 200

@main.route('/library', methods=['POST'])
@login_required
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        read_list_status=data.get('read_list_status', ReadListStatus.UNREAD),
        buy_list_status=data.get('buy_list_status', BuyListStatus.NOT_OWNED),
        user_id=current_user.id
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

# @main.route('/categories', methods=['GET'])
# @login_required
# def add_category():
#     data = request.get_json()
#     new_category = Category(name=data['name'], user_id=current_user.id)
#     db.session.add(new_category)
#     db.session.commit()
#     return jsonify({'message': 'Category added!'}), 201

@main.route('/test', methods = ['GET'])
def run_test():
    test()
    return jsonify({'message': 'Test executed!'}), 201
