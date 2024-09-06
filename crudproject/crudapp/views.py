from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    books = Book.objects.all()
    return render(request, 'crudapp/index.html', {'books': books})

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            published_date=data['published_date']
        )
        return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author, 'published_date': book.published_date})

@csrf_exempt
def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        data = json.loads(request.body)
        book.title = data['title']
        book.author = data['author']
        book.published_date = data['published_date']
        book.save()
        return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author, 'published_date': book.published_date})

@csrf_exempt
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return JsonResponse({'id': id})

def read_books(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)