from django import forms
from blog.models import Savat
from book.models import Book


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Savat
        fields = ['user', 'book', 'title', 'shipping_date', 'count_orders']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'image','price', 'count']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'price', 'count']