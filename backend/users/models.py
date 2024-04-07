from core.constants import LenghtField
from core.validators import username_validator, validate_mobile
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    """
    Модель пользователя с дополнительными полями.
    Атрибуты:
        - USER: Константа для обозначения роли обычного пользователя.
        - ADMIN: Константа для обозначения роли администратора.
        - email: Поле для электронной почты пользователя.
        - username: Поле для логина пользователя.
        - full_name: Поле для полного имени пользователя.
        - phone: Поле для телефонного номера пользователя.
        - first_enter: Флаг первого входа пользователя.
        - icon: Поле для фотографии профиля пользователя.
        - birth_date: Поле для даты рождения пользователя.
        - role: Поле для определения роли пользователя.
    """

    class RoleChoises(models.TextChoices):
        """
        Определение роли юзера.
        """

        USER = "user"
        ADMIN = "admin"

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
    full_name = models.CharField(
        max_length=LenghtField.MAX_LENGHT_FIRST_NAME.value,
        blank=True,
        verbose_name="Полное имя",
    )
    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Телефон",
        unique=True,
        validators=[validate_mobile],
    )

    first_enter = models.BooleanField(
        default=True, verbose_name="Флаг первого входа")
    icon = models.ImageField(
        verbose_name="Фото профиля",
        upload_to="users/profile_photo",
        null=True,
        blank=True,
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="День Рождения пользователя"
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
