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


class ShortCategorySerializer(serializers.ModelSerializer):

    slug = serializers.SlugField(read_only=True)

    class Meta:
        fields = ("name", "slug")
        model = Category


class ServicesSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    tariff = serializers.SerializerMethodField()

    class Meta:
        model = Services
        fields = (
            "id",
            "name",
            "category",
            "link",
            "description",
            "icon_big",
            "icon_square",
            "icon_small",
            "is_popular",
            "tariff"
        )

    def get_tariff(self, obj):
        return TariffListSerializer(obj.tarifflists.all(), many=True).data


class ShortServicesSerializer(serializers.ModelSerializer):
    category = ShortCategorySerializer()

    class Meta:
        fields = ("name", "category")
        model = Services


class TariffListSerializer(serializers.ModelSerializer):
    services_duration = serializers.ChoiceField(
        default=TariffList.Duration.ONE_MONTH, choices=TariffList.Duration
    )

    class Meta:
        fields = "__all__"
        model = TariffList


class ShortTariffListSerializer(serializers.ModelSerializer):
    services = ShortServicesSerializer()
    services_duration = serializers.ChoiceField(
        default=TariffList.Duration.ONE_MONTH, choices=TariffList.Duration
    )

    class Meta:
        fields = ("id", "services_duration", "services")
        model = TariffList


class UserSubscriptionServiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Subscription
