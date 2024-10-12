from django.db import models

from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст', null=True, blank=True)
    alone = models.BooleanField(verbose_name='Одинок', default=True)
    username = models.CharField(max_length=40, unique=True, verbose_name='Пользователь')
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return f'{self.username}'
