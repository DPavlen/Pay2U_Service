import datetime

from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.db import IntegrityError, models
from django.utils.text import slugify
from rest_framework.exceptions import PermissionDenied
from transliterate import translit

from .exceptions import BadRequestException

User = get_user_model()


class Category(models.Model):
    """
    Класс для категории.

    name - название категории
    slug - адрес категории
    description - описание категория
    icon - картинка категории

    """

    name = models.CharField(max_length=20, verbose_name="название категории")
    slug = models.SlugField(max_length=255, unique=True,)
    description = models.CharField(max_length=250, verbose_name="описание категории")
    icon = models.ImageField(
        verbose_name="Фото категории",
        upload_to="category/images/",
        default=None,
        blank=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        """
        Метод для отображения имени категории как строки.
        """

        return self.name

    def save(self, **kwargs):
        """
        Метод для сохранения категории.
        Если slug не указан, то генерируется на основе названия категории.
        Raises:
        - BadRequestException: Если возникает ошибка целостности при сохранении.
        """

        if not self.slug:
            self.slug = slugify(translit(self.name, "ru", reversed=True))
        try:
            super(Category, self).save(**kwargs)
        except IntegrityError:
            raise BadRequestException


class Services(models.Model):
    """
    Класс для сервиса.
    Attributes:
        - name: Название сервиса.
        - category: Категория сервиса.
        - link: Ссылка на сервис.
        - description: Описание сервиса.
        - is_popular: Флаг для определения популярности сервиса.
        - icon_big: Фото сервиса большое.
        - icon_square: Фото сервиса среднее.
        - icon_small: Фото сервиса маленькое.
    """

    name = models.CharField(max_length=250, verbose_name="название")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        null=True
    )
    link = models.URLField(
        verbose_name="ссылка",
        max_length=400,
        blank=True,
        null=True)
    description = models.TextField(
        verbose_name="описание")
    is_popular = models.BooleanField(
        default=False,
        verbose_name="Популярный сервис?")
    icon_big = models.ImageField(
        verbose_name="Фото сервиса большое",
        upload_to="services/images/big/",
        blank=True,
        null=True,
    )
    icon_square = models.ImageField(
        verbose_name="Фото сервиса среднее",
        upload_to="services/images/square/",
        blank=True,
        null=True,
    )
    icon_small = models.ImageField(
        verbose_name="Фото сервиса маленькое",
        upload_to="services/images/small/",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        """
        Метод для отображения имени сервиса как строки.
        """

        return self.name


class TariffList(models.Model):
    """
    Класс для тарифа.
    Attributes:
        - name: Название тарифа.
        - description: Описание тарифа.
        - services: Сервис, к которому привязан тариф.
        - services_duration: Длительность тарифа (в месяцах).
        - tariff_full_price: Полная стоимость тарифа.
        - tariff_promo_price: Промо стоимость тарифа.
    """

    class Duration(models.TextChoices):
        ONE_MONTH = "1", "Один месяц"
        THREE_MONTHS = "3", "Три месяца"
        SIX_MONTHS = "6", "Шесть месяцев"
        ONE_YEAR = "12", "Один год"
    name = models.CharField(
        max_length=250,
        verbose_name="название тарифа")
    description = models.CharField(
        max_length=250,
        verbose_name="описание тарифа")
    services = models.ForeignKey(
        Services,
        on_delete=models.SET_NULL,
        verbose_name="сервис",
        null=True,
        related_name="tarifflists"
    )
    services_duration = models.CharField(
        max_length=20,
        choices=Duration.choices,
        verbose_name="длительность тарифа",
        default=Duration.ONE_MONTH,
    )
    tariff_full_price = models.FloatField(
        verbose_name="полная стоимость тарифа")
    tariff_promo_price = models.FloatField(
        blank=True,
        null=True,
        verbose_name="промо стоимость тарифа")

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"

    def __str__(self):
        return (f"{self.services} длительностью {self.services_duration}")

    def subscribe(self, user, auto_payment=False):
        """
        Метод для подписки на сервис по данному тарифу.
        Args:
            user: Пользователь, который подписывается на сервис.
            auto_payment: Флаг для автоматического продления подписки.
        Returns:
            subscription: Созданный объект подписки.
        Raises:
            PermissionDenied: Если пользователь уже подписан на сервис.
        """

        subscription, created = Subscription.objects.get_or_create(
            user=user, tariff=self, auto_payment=auto_payment
        )
        if not created:
            raise PermissionDenied({"detail": "Already subscribe."})
        return subscription


class Subscription(models.Model):
    """
    Модель для подписки пользователя на сервис.
    created_at - создана подписки
    updated_at - продлена подписка
    user - пользователей который подписался
    service - сервис на который подписались
    status - текущий статус
    """

    class Status(models.TextChoices):
        SUBSCRIBED = "subscribed", "Подписан"
        NOT_SUBSCRIBED = "not_subscribed", "Не подписан"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="subscriptions"
    )
    tariff = models.ForeignKey(
        TariffList,
        on_delete=models.PROTECT,
        related_name="subscriptions"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Подписка активна?"
    )
    auto_payment = models.BooleanField(
        default=False, verbose_name="Автоплотеж")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "tariff"],
                name="unique_user_tariff",
            ),
        ]

        ordering = ("user",)
        verbose_name = "Подписка на сервис"
        verbose_name_plural = "Подписки на сервисы"

    def __str__(self):
        return (f"Пользователь: {self.user.username}, "
                f" на сервис: '{self.tariff.services}' ")

    def check_subscription(self):
        """
        Метод для проверки активности подписки и её продления.
        Returns:
        end_date: Дата окончания текущего периода подписки.
        """

        date = datetime.date.today()
        end_date = self.updated_at.date() + relativedelta(months=+int(self.tariff.services_duration))
        if end_date < date:
            self.is_active = False
            return end_date
        self.is_active = True
        return end_date
