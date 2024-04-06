# Generated by Django 5.0.2 on 2024-04-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0007_alter_subscriptionpayment_expired_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentmethods",
            name="payment_method",
            field=models.TextField(
                choices=[
                    ("СБП", "Sbp"),
                    ("Кредитная карта", "Credit Card"),
                    ("PayPal", "Paypal"),
                    ("Мобильные платежи", "Mobile Payment"),
                    ("Платежные системы криптовалюты", "Cryptocurrency"),
                ],
                default="СБП",
                verbose_name="Способ оплаты подписки",
            ),
        ),
    ]
