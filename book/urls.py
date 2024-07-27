from django.urls import path
from .views import HomeView, BooksView, BookDetailView, CreateBookView, DeleteBookView, CreateBooklistView, \
    UpdateBookView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books/', BooksView.as_view(), name='books'),
    path('books/<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', CreateBookView.as_view(), name='book-create'),
    path('books/delete/<int:id>/', DeleteBookView.as_view(), name='book-delete'),
    path('books/create/list/', CreateBooklistView.as_view(), name='book-create-list'),
    path('books/update/<int:pk>/', UpdateBookView.as_view(), name='book-update'),
]
