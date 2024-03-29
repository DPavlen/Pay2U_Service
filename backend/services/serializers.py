import base64

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from rest_framework import serializers

from .models import Category, Services, Subscription, TariffList

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
    slug = serializers.SlugField(read_only=True)

    class Meta:
        fields = "__all__"
        model = Category


class ServicesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        fields = "__all__"
        model = Services


class TariffListSerializer(serializers.ModelSerializer):
    services = ServicesSerializer()
    services_duration = serializers.ChoiceField(
        default=TariffList.Duration.ONE_MONTH, choices=TariffList.Duration
    )

    class Meta:
        fields = "__all__"
        model = TariffList


class UserSubscriptionServiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Subscription
