from django.db import models

# Create your models here.
class Books(models.Model):
	book_title = models.CharField(max_length=200)
	book_author = models.CharField(max_length=200)
	book_pubtime = models.CharField(max_length=20)
	book_isbn = models.CharField(max_length=13)
	book_borrowid = models.CharField(max_length=5)

	def __str__(self):
		return self.book_title
# 
# class Borrows(models.Model):
# 	user_id = models.CharField(max_length=5)
# 	user_n
