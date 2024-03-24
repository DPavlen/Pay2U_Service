from django.contrib import admin

from .models import Faq


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "answer",
        "created",
        "updated",
        "author",
    )
    list_filter = ("question", "answer", "created", "author")
    search_fields = ("user__username", "question")
