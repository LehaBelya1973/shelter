from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Кличка')
    category = models.CharField(max_length=100, verbose_name='Порода')
    phot = models.IntegerField(upload_to='dogs/', **NULLABLE)
    birth_day = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
