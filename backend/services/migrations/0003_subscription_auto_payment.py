# Generated by Django 5.0.2 on 2024-04-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='auto_payment',
            field=models.BooleanField(default=False, verbose_name='Автоплотеж'),
        ),
    ]
