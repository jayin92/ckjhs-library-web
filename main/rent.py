from .models import Books

def confirm_rent_database(books, username):
	for book in books:
		book.book_borrowid = username
