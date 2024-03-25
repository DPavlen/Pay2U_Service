import csv

from django.core.management.base import BaseCommand
from services.models import Services


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            with open("data/service.csv", encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                for name, services_duration, cost, subscription_type in reader:
                    # try:
                    #     category = Category.objects.get(id=id)
                    # except ObjectDoesNotExist:
                    #     category = None
                    # Вытаскиваем services_duration из Services.Duration
                    if services_duration == "Один месяц":
                        services_duration = Services.Duration.ONE_MONTH
                    elif services_duration == "Три месяца":
                        services_duration = Services.Duration.THREE_MONTHS
                    elif services_duration == "Шесть месяцев":
                        services_duration = Services.Duration.SIX_MONTHS
                    elif services_duration == "Один год":
                        services_duration = Services.Duration.ONE_YEAR

                    Services.objects.get_or_create(
                        name=name,
                        # category=category,
                        services_duration=services_duration,
                        cost=cost,
                        subscription_type=subscription_type,
                    )
        except Exception:
            raise ("Ошибка при загрузке 'Сервисов':")
        return (
            "Загрузка 'Сервисов' произошла успешно!"
            " Обработка файла service.csv завершена."
        )