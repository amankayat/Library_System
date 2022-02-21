from atexit import register
from django.contrib import admin

from books.models import book_data

# Register your models here.

@admin.register(book_data)
class book_dataadmin(admin.ModelAdmin):
    list_display = ['id','name','author','year']
