from django.db import models
from services.models import Services, Subscription
from users.models import MyUser


class PaymentMethods(models.Model):
    """Модель способов оплаты подписок."""

    class PaymentMethodChoises(models.TextChoices):
        """
        Способ оплаты подписки.
        """

        SBP = " SBP", "СБП"
        CREDIT_CARD = "credit_card", "Кредитная карта"
        PAYPAL = "paypal", "PayPal"
        MOBILE_PAYMENT = "mobile_payment", "Мобильные платежи"
        CRYPTOCURRENCY = "cryptocurrency", "Платежные системы криптовалюты"

    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE,
        verbose_name="Подписка",
    )
    payment_method = models.TextField(
        choices=PaymentMethodChoises.choices,
        default=PaymentMethodChoises.SBP,
        max_length=20,
        verbose_name="Способ оплаты подписки",
    )

    class Meta:
        verbose_name = "Метод оплаты подписки"
        verbose_name_plural = "Методы оплаты подписок"
        ordering = ["-id"]

    def __str__(self):
        return (f"Текущая Подписка {self.subscription} ")


class SubscriptionPayment(models.Model):
    """
    Модель для связи между подпиской и оплатой.
    """

    STATUS_CHOICES = (
        ("payment_completed", "Оплата прошла"),
        ("not_paid", "Не оплачено"),
    )
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE,
        verbose_name="Подписка",
        related_name="payments",
    )
    payment_methods = models.ForeignKey(
        PaymentMethods,
        on_delete=models.CASCADE,
        verbose_name="Способ оплаты",
        related_name="subscription_payments",
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма оплаты подписки",
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Даты оплаты подписки"
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="not_paid",
        blank=True,
        verbose_name="Статус оплаты подписки",
    )

    class Meta:
        verbose_name = "Подписка и оплата"
        verbose_name_plural = "Подписки и оплаты"

    def __str__(self):
        return f"{self.payment_methods}"


class Cashback(models.Model):
    """
    Модель получения кэшбека.
    """

    class CashbackType(models.TextChoices):
        """
        Тип кэшбека.
        """

    TYPE_CASHBACK = (
        ("fixed_amount", "Фиксированная сумма"),
        ("percentage", "Процент от суммы платежа")
    )

    STATUS_CASHBACK = (
        ("cashback_completed", "Кешбэк получен"),
        ("cashback_not_received", "Кешбэк не получен"),
    )

    subscription_service = models.OneToOneField(
        Services,
        on_delete=models.CASCADE,
        verbose_name="Сервис подписки"
    )
    payment_methods = models.OneToOneField(
        PaymentMethods,
        on_delete=models.CASCADE,
        verbose_name="Способ оплаты"
    )
    description = models.TextField(
        verbose_name="Текст кэшбека"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Количество кэшбека"
    )
    type_cashback = models.CharField(
        "Тип кэшбека",
        choices=TYPE_CASHBACK,
        default="fixed_amount",
        max_length=155,
    )
    status = models.CharField(
        max_length=100,
        choices=STATUS_CASHBACK,
        default="cashback_not_received",
        verbose_name="Статус получения кэшбека")

    class Meta:
        verbose_name = "Кэшбек"
        verbose_name_plural = "Кэшбеки"
        ordering = ["-id"]

    def __str__(self):
        return str(self.type_cashback)
