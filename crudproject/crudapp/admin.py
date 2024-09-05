from django.contrib import admin
from .models import Book
# Register your models here.

def Book_display(obj):
    list_display = ['title', 'author', 'published_date']

admin.site.register(Book)