from django.db import models

from .author import Author
from .book import Book


class BookAuthor(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.DO_NOTHING, blank=False,
        null=False, related_name='authors', verbose_name='Имя автора'
    )
    book = models.ForeignKey(
        Book, on_delete=models.DO_NOTHING, blank=False,
        null=False, related_name='books', verbose_name='Книга'
    )

    class Meta:
        verbose_name = 'Автор книги'
        verbose_name_plural = 'Авторы книги'

        unique_together = [
            ['author', 'book']
        ]
