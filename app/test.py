# # Anything in this file will run once you hit the api on the '/test' endpoint with a get request.

def test():
    print("Hello World!")

# # Create a user
# new_user = User(name='Alice')
# db.session.add(new_user)
# db.session.commit()

# # Create categories
# category1 = Category(name='Fiction', user_id=new_user.id)
# category2 = Category(name='Science', user_id=new_user.id)
# db.session.add(category1)
# db.session.add(category2)
# db.session.commit()

# # Create a book and associate it with multiple categories
# new_book = Book(title='The Great Gatsby', author='F. Scott Fitzgerald')
# new_book.categories.append(category1)  # Associate with Fiction
# new_book.categories.append(category2)  # Associate with Science
# db.session.add(new_book)
# db.session.commit()

# # Access categories of the book
# for category in new_book.categories:
#     print(category.name)