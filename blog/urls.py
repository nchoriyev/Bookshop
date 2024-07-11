from django.urls import path

from .views import savat

urlpatterns = [
    path('', savat, name='savat'),
]
