# Generated by Django 5.0.2 on 2024-04-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0003_alter_subscriptionpayment_expired_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscriptionpayment",
            name="expired_date",
            field=models.DateField(blank=True, verbose_name="Дата истечения подписки"),
        ),
    ]
