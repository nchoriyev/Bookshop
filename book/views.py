from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, BookForm, UpdateForm
from django.views.generic import TemplateView, ListView, DetailView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home.html'

@method_decorator(login_required, name='dispatch')
class BooksView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'

    def post(self, request):
        search = request.POST.get('search', '')
        self.object_list = self.get_queryset().filter(
            title__icontains=search
        ) | self.get_queryset().filter(
            author__first_name__icontains=search
        )
        context = self.get_context_data()
        context['value'] = search
        if not self.object_list.exists():
            context['message'] = "Not Found"
        else:
            context['message'] = "Successfully"
        return self.render_to_response(context)

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class CreateBookView(CreateView):
    form_class = ArticleForm
    template_name = 'create_book.html'
    success_url = '/books/'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, message="Xatolik topildi"))

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = '/books/'
    pk_url_kwarg = 'id'

    def get(self, request, id):
        return self.post(request, id)

    def post(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return redirect(self.success_url)

class CreateBooklistView(CreateView):
    form_class = BookForm
    template_name = 'create_book_to_list.html'
    success_url = '/books/'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, message="Xatolik topildi"))

class UpdateBookView(UpdateView):
    model = Book
    form_class = UpdateForm
    template_name = 'update_detail.html'
    success_url = '/books/'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, message="Xatolik topildi"))
