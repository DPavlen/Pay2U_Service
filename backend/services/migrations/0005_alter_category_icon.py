# Generated by Django 5.0.2 on 2024-03-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_subscriptionpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, default=None, upload_to='services/images/', verbose_name='Фото категории'),
        ),
    ]
