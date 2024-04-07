from django.contrib import admin

from .models import Faq


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    """
    Настроенная панель админки (вопросы и ответы).
    Attributes:
        list_display (tuple): Поля для отображения в списке объектов Faq.
        list_filter (tuple): Поля для фильтрации списка объектов Faq.
        search_fields (tuple): Поля, по которым осуществляется поиск.
    """

    list_display = (
        "topic_question",
        "question",
        "answer",
        "created",
        "updated",
        "сategory",
    )
    list_filter = ("topic_question", "question", "answer", "created",)
    search_fields = ("topic_question", "question",)
