from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'home.html')

def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(title__icontains=search)
        if books:
            return render(request, 'books.html', {'books': books, "value": search, "message": "Successfully"})
        else:
            return render(request, 'books.html', {'message': "Not Fount"})
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})
