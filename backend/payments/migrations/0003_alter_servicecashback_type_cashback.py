# Generated by Django 5.0.2 on 2024-04-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0002_alter_paymentmethods_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicecashback",
            name="type_cashback",
            field=models.CharField(
                choices=[
                    ("fixed_amount", "Фиксированная сумма"),
                    ("percentage", "Процент от суммы платежа"),
                ],
                default="fixed_amount",
                max_length=155,
                verbose_name="Тип кэшбека",
            ),
        ),
    ]
