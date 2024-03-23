import base64

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Category, Services

User = get_user_model()


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        return super().to_internal_value(data)


class CategorySerializer(serializers.ModelSerializer):
    icon = Base64ImageField(
        required=False,
    )

    class Meta:
        fields = "__all__"
        model = Category


class ServicesSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)
    category = CategorySerializer()
    services_duration = serializers.ChoiceField(
        default=Services.Duration.ONE_MONTH, choices=Services.Duration
    )
    cost = serializers.SerializerMethodField

    class Meta:
        fields = "__all__"
        model = Services
