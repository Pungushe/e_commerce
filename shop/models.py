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

class OrderDetail(models.Model):
    username = models.CharField(max_length=200, verbose_name='Имя пользователя')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар') 
    amount = models.IntegerField(verbose_name='Количество')
    stripe_payment_intent = models.CharField(max_length=200, null=True)
    has_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = verbose_name_plural = 'Детали заказа'

