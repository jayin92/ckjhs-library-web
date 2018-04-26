from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Books(models.Model):
    book_title = models.CharField(blank=True, null=True, max_length=200)
    book_author = models.CharField(blank=True, null=True, max_length=200)
    book_pubtime = models.CharField(blank=True, null=True, max_length=20)
    book_isbn = models.CharField(blank=True, null=True, max_length=13)
    book_borrowid = models.CharField(blank=True, default='', max_length=5)
    book_borrowname = models.CharField(blank=True, default='', max_length=5)
    book_barcode = models.CharField(blank=True, default='', max_length=5)

    def __str__(self):
        return self.book_title


class NewBooks(models.Model):
    book_title = models.CharField(blank=True, default='', max_length=200)
    book_author = models.CharField(blank=True, default='', max_length=200)
    book_pubtime = models.CharField(blank=True, default='', max_length=20)
    book_isbn = models.CharField(blank=True, default='', max_length=13)
    book_borrowid = models.CharField(blank=True, default='', max_length=5)
    book_borrowname = models.CharField(blank=True, default='', max_length=5)
    book_barcode = models.CharField(blank=True, default='', max_length=5)

    def __str__(self):
        return self.book_title


class Borrows(models.Model):
    borrower = models.CharField(max_length=100)
    rent_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='')
    isbn = models.CharField(max_length=100)
    barcode = models.CharField(max_length=10, default='')
    pubtime = models.CharField(max_length=100, default='')
    return_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.borrower


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=5)
    school_id = models.CharField(max_length=5)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
