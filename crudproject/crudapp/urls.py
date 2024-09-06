from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_book, name='create_book'),
    path('update/<int:id>/', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    path('book/<int:id>/', views.read_book, name='read_books'),
    path('books/', views.read_books, name='read_books'),
]
