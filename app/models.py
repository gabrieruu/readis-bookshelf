from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum

book_category = db.Table('book_category',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class ReadListStatus(Enum):
    UNREAD = 'unread'
    TO_READ = 'to_read'
    READ = 'read'

class BuyListStatus(Enum):
    NOT_OWNED = 'not_owned'
    OWNED = 'owned'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    read_list_status = db.Column(db.Enum(ReadListStatus), default=ReadListStatus.UNREAD)
    buy_list_status = db.Column(db.Enum(BuyListStatus), default=BuyListStatus.NOT_OWNED)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', back_populates='books')
    categories = db.relationship('Category', secondary=book_category, back_populates='books')

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    books = db.relationship('Book', back_populates='user')
    categories = db.relationship('Category', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def create_default_categories(self):
        default_categories = ['Fiction', 'Non-Fiction', 'Sci-Fi', 'Fantasy']
        for name in default_categories:
            category = Category(name=name, user=self)
            db.session.add(category)
        db.session.commit()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', back_populates='categories')
    books = db.relationship('Book', secondary=book_category, back_populates='categories')

    def __repr__(self):
        return f'<Category {self.name}>'
