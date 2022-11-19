from django.contrib import admin

from django.db import transaction

from .models import Book, Author, BookAuthor, Order


class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'books_count'
    ]

    @staticmethod
    def books_count(obj):
        return len(obj.book_authors.all())


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = (
        BookAuthorInline,
    )

    list_display = [
        'name', 'count', 'price', 'authors'
    ]

    @staticmethod
    def authors(obj):
        # book_authors = BookAuthor.objects.filter(book=obj)
        # authors_names = [ba.author.name for ba in book_authors]
        # return ', '.join(authors_names)

        # return ', '.join([
        #     ba.author.name for ba in BookAuthor.objects.select_related('author', 'book').filter(book=obj)
        # ])

        return ', '.join(a.name for a in obj.author.all())


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def save_related(self, request, form, formsets, change):
        with transaction.atomic():
            order = Order.objects.create(customer=form.cleaned_data['customer'])
            for book in form.cleaned_data['books']:
                book.count -= 1
                book.full_clean()

                book.save()

                order.books.add(book)
            super().save_related(request, form, formsets, change)
