from .models import Books, Borrows
import django.utils.timezone as timezone
def confirm_rent_database(books, user):
	for book in books:
		print(book.book_borrowid)
		if book.book_borrowid == user.profile.school_id:
			book.book_borrowid = ''
			book.book_borrowname = ''
			borrow = Borrows.objects.get(borrower=user.profile.real_name, isbn=book.book_isbn, return_time=None)
			borrow.return_time = timezone.now()
		else:
			book.book_borrowid = user.profile.school_id
			book.book_borrowname = user.profile.real_name
			borrow = Borrows(borrower = user.profile.real_name,
							 title = book.book_title,
							 isbn  = book.book_isbn,
							 author = book.book_author,
							 pubtime = book.book_pubtime)
		book.save()
		borrow.save()
