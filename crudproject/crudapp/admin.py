from django.contrib import admin
from .models import Book
# Register your models here.

class Book_display(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']

admin.site.register(Book,Book_display)