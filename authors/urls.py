from django.urls import path

from .views import authors, create_author, aythor_update, delete_author, author_detail

urlpatterns = [
    path('', authors, name='book-author'),
    path('create/', create_author, name='author-create'),
    path('books/<int:id>/update_author/', aythor_update, name='author-update'),
    path('books/<int:id>/delete_author/', delete_author, name='author-delete'),
    path('books/<int:id>/detail_author/', author_detail, name='author-detail'),
]
