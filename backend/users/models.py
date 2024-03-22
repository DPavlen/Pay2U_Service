from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumbers import phonenumber

from core.constants import LenghtField
from core.validators import (
    username_validator,
    first_name_validator,
    last_name_validator,
)


class MyUser(AbstractUser):
    """
    Кастомная модель переопределенного юзера.
    Добавлены.
    """
    class RoleChoises(models.TextChoices):
        """
        Определение роли юзера.
        """
        USER = "user"
        ADMIN = "admin"
    # REQUIRED_FIELDS = ["first_name", "last_name", "email"]
    email = models.EmailField(
        max_length=LenghtField.MAX_LENGHT_EMAIL.value,
        unique=True,
        verbose_name="email address",
    )
    username = models.CharField(
        "Логин пользователя",
        max_length=LenghtField.MAX_LENGHT_USERNAME.value,
        unique=True,
        validators=[username_validator],
    )
    phone = phonenumber.PhoneNumber(
    )

    first_name = models.CharField(
        "Имя пользователя",
        max_length=LenghtField.MAX_LENGHT_FIRST_NAME.value,
        null=True,
        blank=True,
        validators=[first_name_validator],
    )
    last_name = models.CharField(
        "Фамилия пользователя",
        max_length=LenghtField.MAX_LENGHT_LAST_NAME.value,
        null=True,
        blank=True,
        validators=[last_name_validator],
    )
    birth_date = models.DateField(
        "День Рождения пользователя",
        null=True,
        blank=True
    )
    password = models.CharField(
        "Пароль пользователя",
        max_length=LenghtField.MAX_LENGHT_PASSWORD.value,
    )
    role = models.TextField(
        "Пользовательская роль юзера",
        choices=RoleChoises.choices,
        default=RoleChoises.USER,
        max_length=LenghtField.MAX_LENGHT_ROLE.value,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-id"]

    def __str__(self):
        return str(self.username)


class UserIcon(models.Model):
    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, verbose_name="Пользователь"
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