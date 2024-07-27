from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import path
from django.views import View
from django.views.generic import FormView, CreateView, RedirectView, TemplateView

class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('home')

    def form_invalid(self, form):
        context = {"message": "Login yoki password xato!"}
        return self.render_to_response(context)

class RegisterView(CreateView):
    model = User
    template_name = 'auth/register.html'
    fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

class ShowUserView(TemplateView):
    template_name = 'show_user.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'username': request.user.username,
                'email': request.user.email
            }
            return self.render_to_response(context)
        else:
            return redirect('login')
