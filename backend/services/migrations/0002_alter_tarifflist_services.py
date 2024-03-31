# Generated by Django 5.0.2 on 2024-03-31 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarifflist",
            name="services",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tarifflists",
                to="services.services",
                verbose_name="сервис",
            ),
        ),
    ]
