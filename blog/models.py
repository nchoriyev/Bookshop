from django.db import models
from django.contrib.auth.models import User
from book.models import Book


class Savat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, max_length=300)
    title = models.CharField(max_length=300)
    shipping_date = models.DateField()
    count_orders = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UserBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BasketBooks(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(default=0)
    total_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_total_price(instance, obj):
        obj.total_price = obj.book.price * obj.count
