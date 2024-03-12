from django.db import models

class Task(models.Model):
    name = models.CharField('Название товара', max_length=100)
    place = models.CharField('Объём', max_length=100, )
    price = models.IntegerField('Цена')
    square = models.IntegerField('Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'