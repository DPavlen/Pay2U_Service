import json

from django.core.management.base import BaseCommand
from services.models import Services


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            with open("data/service.json", encoding="utf-8-sig") as f:
                services_data = json.load(f)
                for service in services_data:
                    name = service.get("name")
                    link = service.get("link")
                    description = service.get("description")
                    is_popular = service.get("is_popular", "FALSE").upper() == "TRUE"
                    Services.objects.get_or_create(
                        name=name,
                        link=link,
                        description=description,
                        is_popular=is_popular
                    )
        except Exception as e:
            raise Exception("Ошибка при загрузке 'Сервисов': {}".format(str(e)))
        return "Загрузка 'Сервисов' произошла успешно! Обработка файла service.json завершена."
