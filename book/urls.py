from django.urls import path

from .views import home, books, book_detail, create_book, delete_book, create_booklist, update_book

urlpatterns = [
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('books/<slug:slug>', book_detail, name='book-detail'),
    path('books/create/', create_book, name='book-create'),
    path('books/<int:id>/delete/', delete_book, name='book-delete'),
    path('books/createlist/', create_booklist, name='book-create-list'),
    path('books/<int:id>/updatelist/', update_book, name='book-update'),
]
