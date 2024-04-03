# Generated by Django 5.0.2 on 2024-04-03 13:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("services", "0002_alter_tarifflist_services"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentMethods",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_method",
                    models.TextField(
                        choices=[
                            (" SBP", "СБП"),
                            ("credit_card", "Кредитная карта"),
                            ("paypal", "PayPal"),
                            ("mobile_payment", "Мобильные платежи"),
                            ("cryptocurrency", "Платежные системы криптовалюты"),
                        ],
                        default=" SBP",
                        max_length=20,
                        verbose_name="Способ оплаты подписки",
                    ),
                ),
                (
                    "icon",
                    models.ImageField(
                        blank=True,
                        default=None,
                        upload_to="payments/images/",
                        verbose_name="Фото Способа оплаты",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services.subscription",
                        verbose_name="Подписка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Метод оплаты подписки",
                "verbose_name_plural": "Методы оплаты подписок",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="ServiceCashback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type_cashback",
                    models.CharField(
                        choices=[
                            ("fixed_amount", "Фиксированная сумма"),
                            ("percentage", "Процент от суммы платежа"),
                        ],
                        default="cashback_not_received",
                        max_length=155,
                        verbose_name="Тип кэшбека",
                    ),
                ),
                (
                    "subscription_service",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services.services",
                        verbose_name="Сервис подписки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Кэшбек сервиса",
                "verbose_name_plural": "Кэшбеки сервисов",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="SubscriptionPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Сумма оплаты подписки",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Даты оплаты подписки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("payment_completed", "Оплата прошла"),
                            ("not_paid", "Не оплачено"),
                        ],
                        default="not_paid",
                        max_length=30,
                        verbose_name="Статус оплаты подписки",
                    ),
                ),
                (
                    "payment_methods",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription_payments",
                        to="payments.paymentmethods",
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to="services.subscription",
                        verbose_name="Подписка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Подписка и оплата",
                "verbose_name_plural": "Подписки и оплаты",
            },
        ),
        migrations.CreateModel(
            name="UserCashback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(verbose_name="Текст кэшбека")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Количество кэшбека",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("cashback_completed", "Кешбэк получен"),
                            ("cashback_not_received", "Кешбэк не получен"),
                        ],
                        default="cashback_not_received",
                        max_length=100,
                        verbose_name="Статус получения кэшбека",
                    ),
                ),
                (
                    "service_cashback",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payments.servicecashback",
                        verbose_name="Кэшбек сервиса",
                    ),
                ),
                (
                    "subscription_payment",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payments.subscriptionpayment",
                        verbose_name="Платеж подписки",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Кэшбек пользователя",
                "verbose_name_plural": "Кэшбеки пользователей",
                "ordering": ["-id"],
            },
        ),
    ]
