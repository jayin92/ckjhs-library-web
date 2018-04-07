from django.contrib import admin
from .models import Books, Borrows
# Register your models here.

admin.site.register(Books)
admin.site.register(Borrows)
