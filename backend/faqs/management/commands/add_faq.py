import csv

from django.core.management.base import BaseCommand
from faqs.models import Faq


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            with open("data/faq.csv", encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                for topic_question, question, answer in reader:
                    Faq.objects.get_or_create(
                        topic_question=topic_question,
                        question=question,
                        answer=answer,
                    )
        except Exception:
            raise ("Ошибка при загрузке 'FAQS':")
        return (
            "Загрузка 'FAQS' произошла успешно!"
            " Обработка файла faq.csv завершена."
        )
