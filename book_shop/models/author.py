from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False, verbose_name="Имя автора")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
