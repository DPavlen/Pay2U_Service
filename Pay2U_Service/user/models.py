from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(null=True, blank=True, unique=True)
    login = models.CharField(max_length=25, blank=True, verbose_name="Логин")
    full_name = models.CharField(max_length=255, blank=True, verbose_name="Полное имя")
    phone = PhoneNumberField(
        max_length=20, null=True, blank=True, verbose_name="Телефон"
    )
    first_enter = models.BooleanField(default=True, tverbose_name="Флаг первого фхода")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ("-id",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserIcon(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    icon = models.ImageField(
        verbose_name="Фото профиля", upload_to="users/profile_photo"
    )

    def __str__(self):
        return self.user

    class Meta:
        ordering = ("-id",)
        verbose_name = "Фотография пользователя"
        verbose_name_plural = "Фотографии пользователей"
