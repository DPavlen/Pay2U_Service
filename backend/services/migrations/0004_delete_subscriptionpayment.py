# Generated by Django 5.0.2 on 2024-04-07 17:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0003_subscription_auto_payment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SubscriptionPayment",
        ),
    ]
