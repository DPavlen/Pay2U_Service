from django.contrib import admin

from .models import Faq


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = (
        "topic_question",
        "question",
        "answer",
        "created",
        "updated",
    )
    list_filter = ("topic_question", "question", "answer", "created",)
    search_fields = ("topic_question", "question",)
