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
            "topic_question",
            "question",
            "answer",
            "created",
            "updated",
        )
        read_only_fields = ("__all__",)
