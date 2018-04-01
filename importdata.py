from main.models import Books

import sqlite3

conn = sqlite3.connect('library.db')
c = conn.cursor()
c.execute("SELECT * FROM "+'book')
rows = c.fetchall()
bookdata = [list(t) for t in rows]

for book in bookdata:
	q = Books(book_title = book[0],
			  book_author = book[1],
			  book_pubtime = book[2],
			  book_isbn = book[3],
			  book_borrowid = book[4],)
	
	q.save()
