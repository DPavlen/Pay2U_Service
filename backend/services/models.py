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
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(translit(self.name, "ru", reversed=True))
        try:
            super(Category, self).save(**kwargs)
        except IntegrityError:
            raise BadRequestException


class Services(models.Model):
    """
    Класс для сервиса.
    name - название сервиса
    category - категория сервиса
    link - ссылка на сервис на сервис
    description - описание сервиса
    icon - иконка категории
    """

    name = models.CharField(max_length=250, verbose_name="название")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, verbose_name="категория", null=True
    )
    link = models.URLField(verbose_name="ссылка", max_length=400, blank=True, null=True)
    description = models.CharField(max_length=250, verbose_name="описание")
    is_popular = models.BooleanField(default=False, verbose_name="Популярный сервис?")
    icon_big = models.ImageField(
        verbose_name="Фото сервиса большое",
        upload_to="services/images/big/",
        blank=True,
        null=True,
    )
    icon_square = models.ImageField(
        verbose_name="Фото сервиса",
        upload_to="services/images/square/",
        blank=True,
        null=True,
    )
    icon_small = models.ImageField(
        verbose_name="Фото сервиса",
        upload_to="services/images/small/",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return self.name


class TariffList(models.Model):

    class Duration(models.TextChoices):
        ONE_MONTH = "1", "Один месяц"
        THREE_MONTHS = "3", "Три месяца"
        SIX_MONTHS = "6", "Шесть месяцев"
        ONE_YEAR = "12", "Один год"
    name = models.CharField(max_length=250, verbose_name="название тарифа")
    description = models.CharField(max_length=250, verbose_name="описание тарифа")
    services = models.ForeignKey(
        Services, on_delete=models.CASCADE, verbose_name="сервис", related_name="tarifflists"
    )
    services_duration = models.CharField(
        max_length=20,
        choices=Duration.choices,
        verbose_name="длительность тарифа",
        default=Duration.ONE_MONTH,
    )
    tariff_full_price = models.FloatField(verbose_name="полная стоимость тарифа")
    tariff_promo_price = models.FloatField(verbose_name="промо стоимость тарифа")

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"

    def __str__(self):
        return (f"{self.services} длительностью {self.services_duration}")

    def subscribe(self, user):
        """Подписаться на сервис."""
        subscription, created = Subscription.objects.get_or_create(
            user=user, tariff=self
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
    tariff = models.ForeignKey(TariffList, on_delete=models.PROTECT, related_name="subscriptions")
    is_active = models.BooleanField(default=True, verbose_name="Подписка активна?")

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
        date = datetime.date.today()
        end_date = self.updated_at.date() + relativedelta(months=+int(self.tariff.services_duration))
        if end_date < date:
            self.is_active = False
            return end_date
        self.is_active = True
        return end_date


class SubscriptionPayment(models.Model):
    """
    Модель для связи подписки и оплаты сервиса.

    """

    pass
