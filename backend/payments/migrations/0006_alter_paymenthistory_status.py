# Generated by Django 5.0.2 on 2024-03-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0005_alter_paymenthistory_payment_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymenthistory",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("payment_completed", "Оплата прошла"),
                    ("not_paid", "Не оплачено"),
                ],
                default="active",
                max_length=30,
                verbose_name="Статус оплаты подписки",
            ),
        ),
    ]
