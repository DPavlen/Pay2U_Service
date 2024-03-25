from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import PermissionDenied

User = get_user_model()


class Category(models.Model):
    """
    Класс для категории.

    name - название категории
    description - описание категория
    icon - картинка категории

    """

    objects = None
    name = models.CharField(max_length=20, verbose_name="название")
    description = models.CharField(max_length=250, verbose_name="описание")
    icon = models.ImageField(
        verbose_name="Фото категории",
        upload_to="services/images/",
        default=None,
        blank=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Services(models.Model):
    """
    Класс для сервиса.

    name - название сервиса
    category - категория сервиса
    services_duration - длительность подписки на сервис
    cost - стоимость за 1 месяц
    subscription_type - тип подписки.
    """

    objects = None

    class Duration(models.TextChoices):
        ONE_MONTH = "one_month", "Один месяц"
        THREE_MONTHS = "three_months", "Три месяца"
        SIX_MONTHS = "six_months", "Шесть месяцев"
        ONE_YEAR = "one_year", "Один год"

    name = models.CharField(max_length=250, verbose_name="название")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, verbose_name="категория", null=True
    )
    services_duration = models.CharField(
        max_length=20,
        choices=Duration.choices,
        verbose_name="длительность подписки",
        default=Duration.ONE_MONTH,
    )
    cost = models.FloatField(verbose_name="стоимость одного месяца")
    subscription_type = models.CharField(
        max_length=250, verbose_name="тип подписки", null=True, blank=True
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
            raise PermissionDenied({"detail": "Already enrolled."})
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

    objects = None

    class Status(models.TextChoices):
        ENROLLED = "enrolled", "Подписан"
        NOT_ENROLLED = "not_enrolled", "Не подписан"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="subscriptions"
    )
    service = models.ForeignKey(Services, on_delete=models.PROTECT, related_name="+")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        verbose_name="статус подписки",
        default=Status.ENROLLED,
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

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.service_id = None
        self.id = None
        self.user_id = None

    def __str__(self):
        return f"<Subscription: {self.id}, user: {self.user_id}, service: {self.service_id}>"


class SubscriptionPayment(models.Model):
    """
    Модель для связи подписки и оплаты сервиса.

    """

    pass
