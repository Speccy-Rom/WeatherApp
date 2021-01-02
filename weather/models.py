from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Погода в городе'
        verbose_name_plural = 'Погода в городах'
        ordering = ['name']
