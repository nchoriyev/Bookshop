from django.urls import path

from .views import home, books, book_detail

urlpatterns = [
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('books/<slug:slug>', book_detail, name='book-detail'),
]
