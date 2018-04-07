from .models import Books, Borrows
import django.utils.timezone as timezone
def confirm_rent_database(books, username):
	for book in books:
		print(book.book_borrowid)
		if book.book_borrowid == username:
			book.book_borrowid = ''
			borrow = Borrows.objects.get(borrower=username, isbn=book.book_isbn, return_time=None)
			borrow.return_time = timezone.now()
		else:
			book.book_borrowid = username
			borrow = Borrows(borrower = username,
							 title = book.book_title,
							 isbn  = book.book_isbn,
							 author = book.book_author,
							 pubtime = book.book_pubtime)
		book.save()
		borrow.save()
