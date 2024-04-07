import base64

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from rest_framework import serializers

from .models import Category, Services, Subscription, TariffList

User = get_user_model()


class Base64ImageField(serializers.ImageField):
    """
    Поле для обработки изображений в формате base64.
    Если переданные данные начинаются с 'data:image',
    то данные преобразуются из формата base64 в изображение.
    Attributes:
        - data: Данные, содержащие изображение.
    """

    def to_internal_value(self, data):
        """
        Преобразует данные внутреннего представления.
        Args:
        data: Входные данные, содержащие изображение.
        Returns:
        Преобразованные данные.
        """

        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
            ext = format.split("/")[-1]
            data = ContentFile(base64.b64decode(imgstr), name="temp." + ext)

        return super().to_internal_value(data)


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category.
    Attributes:
        - icon: Поле для изображения категории в формате base64.
        - slug: Поле для slug категории (только чтение).
    """

    icon = Base64ImageField(
        required=False,
    )
    slug = serializers.SlugField(read_only=True)

    class Meta:
        fields = "__all__"
        model = Category


class ShortCategorySerializer(serializers.ModelSerializer):
    """
    Короткий сериализатор для модели Category.
    Attributes:
        - slug: Поле для slug категории (только чтение).
    """

    slug = serializers.SlugField(read_only=True)

    class Meta:
        fields = ("name", "slug")
        model = Category


class ServicesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Services.
    Attributes:
        - category: Сериализатор для поля category.
        - tariff: Метод сериализации для поля tariff.
    """

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
        """
        Метод сериализации для поля tariff.
        """

        return TariffListSerializer(obj.tarifflists.all(), many=True).data


class ShortServicesSerializer(serializers.ModelSerializer):
    """
    Краткий сериализатор для модели Services.
    Attributes:
        - category: Краткий сериализатор для поля category.
    """

    category = ShortCategorySerializer()

    class Meta:
        model = Services
        fields = (
            "id",
            "name",
            "category",
            "link",
            "is_popular",
            "icon_big",
            "icon_square",
            "icon_small",
        )


class TariffListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели TariffList.
    Attributes:
        - services_duration: Поле выбора для продолжительности услуги.
        - services: Краткий сериализатор для поля services.
    """

    services_duration = serializers.ChoiceField(
        default=TariffList.Duration.ONE_MONTH,
        choices=TariffList.Duration
    )
    services = ShortServicesSerializer()

    class Meta:
        fields = "__all__"
        model = TariffList


class ShortTariffListSerializer(serializers.ModelSerializer):
    """
    Краткий сериализатор для модели TariffList.
    Attributes:
        - services: Краткий сериализатор для поля services.
        - services_duration: Поле выбора для продолжительности услуги.
    """

    services = ShortServicesSerializer()
    services_duration = serializers.ChoiceField(
        default=TariffList.Duration.ONE_MONTH, choices=TariffList.Duration
    )

    class Meta:
        model = TariffList
        fields = (
            "id",
            "services_duration",
            "services")


class UserSubscriptionServiceSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели подписки пользователя на сервис.
    Attributes:
        - tariff: Сериализатор тарифа.
        - expired_date: Поле для получения даты истечения подписки.
    """

    tariff = TariffListSerializer()
    expired_date = serializers.SerializerMethodField()

    class Meta:
        fields = (
            "id",
            "created_at",
            "updated_at",
            "user",
            "tariff",
            "is_active",
            "expired_date",
            "auto_payment",
        )
        model = Subscription

    def get_expired_date(self, obj):
        """
        Метод для получения даты истечения подписки.
        Returns: datetime.date: Дата истечения подписки.
        """

        return obj.payments.last().expired_date
