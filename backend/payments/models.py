from django.db import models
from services.models import Services, Subscription, TariffList
from users.models import MyUser


class PaymentMethods(models.Model):
    """
    Модель способов оплаты подписок.
    Attributes:
        - PaymentMethodChoises: Класс перечисления доступных способов оплаты.
        - user: Пользователь, к которому привязан способ оплаты.
        - payment_method: Выбранный способ оплаты.
        - icon: Иконка способа оплаты.
    """

    class PaymentMethodChoises(models.TextChoices):
        """
        Перечисление доступных способов оплаты.
        Attributes:
            - SBP: Система быстрых платежей.
            - CREDIT_CARD: Кредитная карта.
            - PAYPAL: Сервис PayPal.
            - MOBILE_PAYMENT: Мобильные платежи.
            - CRYPTOCURRENCY: Платежные системы криптовалюты.
        """

        SBP = "СБП"
        CREDIT_CARD = "MasterCard **** 1324"
        PAYPAL = "PayPal"
        MOBILE_PAYMENT = "Мобильные платежи"
        CRYPTOCURRENCY = "Платежные системы криптовалюты"

    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    payment_method = models.TextField(
        choices=PaymentMethodChoises.choices,
        default=PaymentMethodChoises.SBP.value,
        verbose_name="Способ оплаты подписки",
    )
    icon = models.ImageField(
        verbose_name="Фото cпособа оплаты",
        upload_to="payments/images/",
        default=None,
        blank=True,
    )

    class Meta:
        verbose_name = "Метод оплаты подписки"
        verbose_name_plural = "Методы оплаты подписок"
        ordering = ["-id"]

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        Returns:
        str: Строковое представление объекта.
        """
        return (f" У юзера {self.user} способ оплаты"
                f" подписки {self.payment_method} ")


class SubscriptionPayment(models.Model):
    """
    Модель для связи между подпиской и оплатой.
    Attributes:
        - subscription: Связанная подписка.
        - payment_methods: Способ оплаты подписки.
        - cost: Сумма оплаты подписки.
        - date: Дата оплаты подписки.
        - expired_date: Дата истечения подписки.
        - status: Статус оплаты подписки.
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
    expired_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата истечения подписки"
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

        """
        Возвращает строковое представление объекта.
        Returns:
        str: Строковое представление объекта.
        """

        return (f"Подписка {self.subscription} "
                f" способ оплаты{self.payment_methods}")


class ServiceCashback(models.Model):
    """
    Модель кэшбэка сервиса.
    Attributes:
        - service_cashback: Сервис, к которому привязывается кэшбэк.
        - type_cashback: Тип кэшбэка.
        - amount_cashback: Количество кэшбэка по тарифу.
    """

    TYPE_CASHBACK = (
        ("fixed_amount", "Фиксированная сумма"),
        ("percentage", "Процент от суммы платежа")
    )
    service_cashback = models.OneToOneField(
        Services,
        on_delete=models.CASCADE,
        verbose_name="Кэшбек сервиса"
    )
    type_cashback = models.CharField(
        "Тип кэшбека",
        choices=TYPE_CASHBACK,
        default="percentage",
        max_length=155
    )
    amount_cashback = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Количество кэшбека по тарифу"
    )

    class Meta:
        verbose_name = "Кэшбек сервиса"
        verbose_name_plural = "Кэшбеки сервисов"
        ordering = ["-id"]

    def __str__(self):

        """
        Возвращает строковое представление объекта.
        Returns: str: Строковое представление объекта.
        """

        return (f"Сервис: {self.service_cashback}"
                f" имеет количество кэшбека по тарифу {self.amount_cashback}")


class UserCashback(models.Model):
    """
    Модель кэшбэка пользователя.
    Attributes:
        - tariff_cashback: Тариф сервиса.
        - user: Пользователь.
        - subscription_payment: Платеж подписки.
        - description: Текст кэшбэка.
        - amount: Количество кэшбэка.
        - status: Статус получения кэшбэка.
    """

    STATUS_CASHBACK = (
        ("cashback_completed", "Кешбэк получен"),
        ("cashback_not_received", "Кешбэк не получен"),
    )
    tariff_cashback = models.OneToOneField(
        TariffList,
        on_delete=models.CASCADE,
        verbose_name="Тариф сервиса"
    )
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name="Пользователь")
    subscription_payment = models.OneToOneField(
        SubscriptionPayment,
        on_delete=models.CASCADE,
        verbose_name="Платеж подписки")
    description = models.TextField(
        blank=True,
        verbose_name="Текст кэшбека")
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Количество кэшбека"
    )
    status = models.CharField(
        "Статус получения кэшбека",
        max_length=100,
        choices=STATUS_CASHBACK,
        default="cashback_not_received",
    )

    class Meta:
        verbose_name = "Кэшбек пользователя"
        verbose_name_plural = "Кэшбеки пользователей"
        ordering = ["-id"]

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        Returns: str: Строковое представление объекта.
        """

        return (f" Пользователем {self.user} за {self.tariff_cashback} "
                f" {self.status} ")