from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, BookForm, UpdateForm


def home(request):
    return render(request, 'home.html')


@login_required()
def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(title__icontains=search) | Book.objects.filter(author__first_name__icontains=search)
        if books:
            return render(request, 'books.html', {'books': books, "value": search, "message": "Successfully"})
        else:
            return render(request, 'books.html', {'message': "Not Fount"})
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    if book:
        return render(request, 'book_detail.html', {'book': book, 'message': "Successfully"})
    else:
        return render(request, 'book_detail.html', {'message': "Not Found"})


def create_book(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
        else:
            return render(request, 'create_book.html', {'form': form, "message": "Xatolik topildi"})
    form = ArticleForm()
    return render(request, 'create_book.html', {'form': form})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')


def create_booklist(request):
    if request.method == 'POST':
        formm = BookForm(request.POST, request.FILES)
        if formm.is_valid():
            formm.save()
            return redirect('books')
        else:
            return render(request, 'create_book_to_list.html', {'formm': formm, "message": "Xatolik topildi"})
    formm = BookForm()
    return render(request, 'create_book_to_list.html', {'formm': formm})

def update_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
        else:
            return render(request, 'update_detail.html', {'form': form, "message": "Xatolik topildi"})
    form = BookForm()
    return render(request, 'update_detail.html', {'form': form})