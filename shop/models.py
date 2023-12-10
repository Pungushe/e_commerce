from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    seller=models.ForeignKey(User, on_delete=models.CASCADE, default='2', verbose_name='Продавец')
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(blank=True, upload_to='images', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

