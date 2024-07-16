from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from blog.models import Savat
from django.contrib.auth.models import User
# from forms import ArticleForm


@login_required()
def savat(request):
    user = request.user
    items = Savat.objects.filter(user=user)
    if User:
        if items:
            return render(request, 'savat.html', {'items': items, 'message': 'Succesfully'})
        else:
            return render(request, 'savat.html', {'message': 'Not Fount'})
    else:
        return 'login'

