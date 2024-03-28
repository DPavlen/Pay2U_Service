from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from rest_framework.exceptions import PermissionDenied

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
            self.slug = slugify(self.name)
        super(Category, self).save(**kwargs)


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
    icon = models.ImageField(
        verbose_name="Фото сервиса",
        upload_to="services/images/",
        default=None,
        blank=True,
    )

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return self.name

    def subscribe(self, user):
        """Подписаться на сервис."""
        subscription, created = Subscription.objects.get_or_create(
            user=user, service=self
        )
        if not created:
            raise PermissionDenied({"detail": "Already subscribe."})
        return subscription


class TariffList(models.Model):

    class Duration(models.TextChoices):
        ONE_MONTH = "one_month", "Один месяц"
        THREE_MONTHS = "three_months", "Три месяца"
        SIX_MONTHS = "six_months", "Шесть месяцев"
        ONE_YEAR = "one_year", "Один год"
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
        return self.name


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
    service = models.ForeignKey(Services, on_delete=models.PROTECT, related_name="+")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        verbose_name="статус подписки",
        default=Status.SUBSCRIBED,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "service"],
                name="unique_user_service",
            ),
        ]

        ordering = ("user",)
        verbose_name = "Подписка на сервис"
        verbose_name_plural = "Подписки на сервисы"

    def __str__(self):
        return (f"Пользователь: {self.user.username}, "
                f" на сервис: '{self.service.name}' "
                f" {self.get_status_display()}")


class SubscriptionPayment(models.Model):
    """
    Модель для связи подписки и оплаты сервиса.

    """

    pass
