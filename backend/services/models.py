from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Category(models.Model):
    """
    Класс для категории.

    name - название категории
    description - описание категория
    icon - картинка категории

    """

    name = models.CharField(max_length=20, verbose_name="название")
    description = models.CharField(max_length=250, verbose_name="описание")
    icon = models.ImageField(
        verbose_name="Фото категории", upload_to="services/services_photo"
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


class FAQ(models.Model):
    """
    Класс для хранения списка часто задаваемых вопросов.

    question - часто задаваемый вопрос
    answer - ответ на заданный вопрос
    created_at - дата создания вопроса
    updated_at - дата обновленя вопроса
    author - пользователь, создавший вопрос/ответ.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    question = models.CharField(max_length=250, verbose_name="Вопрос")
    answer = models.CharField(max_length=1000, verbose_name="Ответ")
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Создатель вопроса"
    )

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __str__(self):
        return self.question


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

    def __str__(self):
        return f"<Subscription: {self.id}, user: {self.user_id}, service: {self.service_id}>"
