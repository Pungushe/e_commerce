from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(blank=True, upload_to='_profile_images', verbose_name='Изображение')
    contact_number = models.CharField(max_length=50, default='+345678912', verbose_name='Номер телефона')
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


