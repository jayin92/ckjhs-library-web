from .models import Books

def confirm_rent_database(books, username):
	for book in books:
		print(book.book_borrowid)
		if book.book_borrowid == username:
			book.book_borrowid = ''
		else:
			book.book_borrowid = username
		book.save()
