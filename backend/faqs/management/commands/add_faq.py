import json

from django.core.management.base import BaseCommand
from faqs.models import Faq


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            with open("data/faq.json", encoding="utf-8-sig") as f:
                faqs_data = json.load(f)
                for faq in faqs_data:
                    topic_question = faq.get("topic_question")
                    question = faq.get("question")
                    answer = faq.get("answer")
                    Faq.objects.get_or_create(
                        topic_question=topic_question,
                        question=question,
                        answer=answer,
                    )
        except Exception:
            raise ("Ошибка при загрузке 'FAQS':")
        return (
            "Загрузка 'FAQS' произошла успешно!"
            " Обработка файла faq.json завершена."
        )
