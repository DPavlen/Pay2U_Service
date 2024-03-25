import csv

from django.core.management.base import BaseCommand
from services.models import Category


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            with open("data/category.csv", encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                for name, description in reader:
                    Category.objects.get_or_create(name=name, description=description)
        except Exception:
            raise ("Ошибка при загрузке 'Категорий':")
        return (
            "Загрузка 'Категорий' произошла успешно!"
            " Обработка файла category.csv завершена."
        )
