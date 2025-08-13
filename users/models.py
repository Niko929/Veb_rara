from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Полностью удаляем поле username
    username = None

    # Делаем email уникальным и используем для входа
    email = models.EmailField('Email', unique=True)

    # Дополнительные поля
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'  # Используем email для входа
    REQUIRED_FIELDS = []  # Убираем username из обязательных полей

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email