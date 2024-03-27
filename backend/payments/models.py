from django.db import models
from services.models import Services, Subscription
from users.models import MyUser


class PaymentHistory(models.Model):
    """Модель истории оплаты подписки."""

    class PaymentMethodChoises(models.TextChoices):
        """
        Способ оплаты подписки.
        """

        SBP = " SBP", "СБП"
        CREDIT_CARD = "credit_card", "Кредитная карта"
        PAYPAL = "paypal", "PayPal"
        MOBILE_PAYMENT = "mobile_payment", "Мобильные платежи"
        CRYPTOCURRENCY = "cryptocurrency", "Платежные системы криптовалюты"

    STATUS_CHOICES = (
        ("payment_completed", "Оплата прошла"),
        ("not_paid", "Не оплачено"),
    )

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
        default=PaymentMethodChoises.CREDIT_CARD,
        max_length=20,
        verbose_name="Способ оплаты подписки",
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Количество",
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Способ оплаты подписки"
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="payment_completed",
        blank=True,
        verbose_name="Статус оплаты подписки",
    )

    class Meta:
        verbose_name = "История оплаты подписки"
        verbose_name_plural = "История оплат подписок"
        ordering = ["-id"]

    def __str__(self):
        return (f"Текущая Подписка {self.subscription} "
                f"и статус оплаты: {self.get_status_display()}")


class SubscriptionPayment(models.Model):
    """
    Модель для связи между подпиской и историей оплаты.
    """

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE,
        verbose_name="Подписка",
        related_name="payments",
    )
    payment_history = models.ForeignKey(
        PaymentHistory,
        on_delete=models.CASCADE,
        verbose_name="История оплаты",
        related_name="subscription_payments",
    )

    class Meta:
        verbose_name = "Подписка и оплата"
        verbose_name_plural = "Подписки и оплаты"

    def __str__(self):
        return f"{self.payment_history}"


class Cashback(models.Model):
    """
    Модель получения кэшбека.
    """

    class CashbackType(models.TextChoices):
        """
        Тип кэшбека.
        """

        FIXED_AMOUNT = "fixed_amount", "Фиксированная сумма"
        PERCENTAGE = "percentage", "Процент от суммы платежа"

    STATUS_CASHBACK = (
        ("cashback_completed", "Кешбэк получен"),
        ("cashback_not_received", "Кешбэк не получен"),
    )

    subscription_service = models.OneToOneField(
        Services, on_delete=models.CASCADE, verbose_name="Сервис подписки"
    )
    payment = models.OneToOneField(
        PaymentHistory, on_delete=models.CASCADE, verbose_name="История оплаты подписки"
    )
    description = models.TextField(verbose_name="Текст кэшбека")
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Количество кэшбека"
    )
    type_cashback = models.CharField(
        "Тип кэшбека",
        choices=CashbackType.choices,
        default=CashbackType.FIXED_AMOUNT,
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
