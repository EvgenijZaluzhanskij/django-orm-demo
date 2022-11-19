from django.db import models
from django.core.exceptions import ValidationError

from .author import Author


def greater_than_zero(value):
    if value < 0:
        raise ValidationError("value can't be less than zero")


class Book(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False, verbose_name="Название книги")
    count = models.BigIntegerField(default=0, verbose_name="Количество на складе", validators=[greater_than_zero])
    price = models.BigIntegerField(validators=[greater_than_zero], verbose_name="Стоимость")
    author = models.ManyToManyField(Author, related_name='book_authors', through='BookAuthor')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
