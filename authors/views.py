from django.shortcuts import render, redirect
from book.models import Author
from .forms import AuthorForm, UpdateAuthorForm

def authors(request):
    if request.method == 'POST':
        search = request.POST['search']
        authors = Author.objects.filter(title__icontains=search) | Author.objects.filter(author__first_name__icontains=search)
        if authors:
            return render(request, 'authors.html', {'authors': authors, "value": search, "message": "Successfully"})
        else:
            return render(request, 'authors.html', {'message': "Not Fount"})
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-author')
        else:
            return render(request, 'create_author.html', {'form': form, "message": "Xatolik topildi"})
    form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})

def aythor_update(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        formmm = UpdateAuthorForm(request.POST, request.FILES, instance=author)
        if formmm.is_valid():
            formmm.save()
            return redirect('book-author')
        else:
            return render(request, 'update_author.html', {'formmm': formmm, "message": "Xatolik topildi"})
    formmm = AuthorForm()
    return render(request, 'update_author.html', {'formmmm': formmm})

def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('book-author')

def author_detail(request, id):
    authorr = Author.objects.get(id=id)
    if authorr:
        return render(request, 'author_detail.html', {'author': authorr, 'message': "Successfully"})
    else:
        return render(request, 'author_detail.html', {'author': authorr, 'message': "Not Fount"})