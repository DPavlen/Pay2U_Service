from django.db import models
from services.models import Services, Subscription
from users.models import MyUser


class PaymentHistory(models.Model):
    """Модель истории оплаты подписки."""

    class PaymentMethodChoises(models.TextChoices):
        """
        Способ оплаты подписки.
        """

        CREDIT_CARD = "credit_card", "Кредитная карта"
        PAYPAL = "paypal", "PayPal"
        MOBILE_PAYMENT = "mobile_payment", "Мобильные платежи"
        CRYPTOCURRENCY = "cryptocurrency", "Платежные системы криптовалюты"

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    payment_method = models.TextField(
        "Способ оплаты подписки",
        choices=PaymentMethodChoises.choices,
        default=PaymentMethodChoises.CREDIT_CARD,
        max_length=155,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=155)

    class Meta:
        verbose_name = "История оплаты подписки"
        verbose_name_plural = "История оплат подписок"
        ordering = ["-id"]

    def __str__(self):
        return str(self.subscription)


class Cashback(models.Model):
    """Модель получения кэшбека."""

    class CashbackType(models.TextChoices):
        """
        Тип кэшбека.
        """

        FIXED_AMOUNT = "fixed_amount", "Фиксированная сумма"
        PERCENTAGE = "percentage", "Процент от суммы платежа"

    subscription_service = models.OneToOneField(Services, on_delete=models.CASCADE)
    payment = models.OneToOneField(PaymentHistory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type_cashback = models.CharField(
        "Тип кэшбека",
        choices=CashbackType.choices,
        default=CashbackType.FIXED_AMOUNT,
        max_length=155,
    )
    status = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Кэшбек"
        verbose_name_plural = "Кэшбеки"
        ordering = ["-id"]

    def __str__(self):
        return str(self.type_cashback)
