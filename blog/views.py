from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from blog.models import Savat
from django.contrib.auth.models import User


@login_required()
def savat(request):
    items = Savat.objects.all()
    if User:
        if items:
            return render(request, 'savat.html', {'items': items, 'message': 'Succesfully'})
        else:
            return render(request, 'savat.html', {'items': items, 'message': 'Sizda faol buyurtmalar yoq'})
    else:
        return 'login'


