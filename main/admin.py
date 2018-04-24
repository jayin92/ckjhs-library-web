from django.contrib import admin
from .models import Books, Borrows, NewBooks
# Register your models here.

admin.site.register(Books)
admin.site.register(NewBooks)
admin.site.register(Borrows)

