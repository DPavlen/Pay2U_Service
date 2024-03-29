# Generated by Django 5.0.2 on 2024-03-29 19:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_alter_category_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='subscription',
            name='unique_user_service',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='service',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='status',
        ),
        migrations.AddField(
            model_name='subscription',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Подписка активна?'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='tariff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='services.tarifflist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('user', 'tariff'), name='unique_user_tariff'),
        ),
    ]
