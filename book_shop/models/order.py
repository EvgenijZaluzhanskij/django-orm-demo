from django.db import models

from .book import Book


class Order(models.Model):
    customer = models.CharField(max_length=1024, null=False, blank=False, verbose_name="Заказчик")
    books = models.ManyToManyField(Book, related_name='ordered_books', null=False, blank=False)