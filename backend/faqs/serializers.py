from faqs.models import Faq
from rest_framework import serializers


class FaqSerializer(serializers.ModelSerializer):
    """
    Сериализатор для часто задаваемых вопросов.
    """

    class Meta:
        model = Faq
        fields = (
            "id",
            "question",
            "answer",
            "created",
            "updated",
            "author",
        )
        read_only_fields = ("__all__",)
