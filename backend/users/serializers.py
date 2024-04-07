from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from users.models import MyUser


class CustomUserSerializer(UserCreateSerializer):
    """
    Сериализатор работы с пользователями.

    Сериализатор, расширяющий базовый сериализатор пользователя,
    для обработки дополнительных полей.

    Attributes:
        - Meta: Класс метаданных для определения модели и полей сериализатора.
    """

    class Meta:
        model = MyUser
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "first_enter",
        )
        extra_kwargs = {
            "email": {"required": False},
            "username": {"required": True},
            "first_name": {"required": False},
            "last_name": {"required": False},
            "password": {"write_only": True,
                         "required": False},
        }

    def create(self, validated_data):
        user = MyUser(
            email=validated_data.get("email"),
            username=validated_data.get("username"),
        )
        user.set_password(validated_data.get("password"))
        user.save()
        return user


class CustomUserReadSerializer(serializers.ModelSerializer):
    """
    Сериализатор для чтения пользователей.
    Сериализатор, предназначенный только для чтения данных пользователя.
    Attributes:
        - Meta: Класс метаданных для определения модели и полей сериализатора.
    """

    class Meta:
        model = MyUser
        fields = ("id", "first_name", "last_name")


class ShortUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для чтения пользователей.
    Сериализатор, предназначенный только для чтения данных пользователя.
    Attributes:
        - Meta: Класс метаданных для определения модели и полей сериализатора.
    """

    class Meta:
        model = MyUser
        fields = (
            "id",
            "username",
            "email",
            "full_name",
        )


class UpdateUserSerializer(UserSerializer):
    """
    Сериализатор обновления пользователей.
    Используется для просмотра и обновления данных существующего пользователя.
    Атрибуты:
        - Meta: Класс метаданных для определения модели и полей сериализатора.
    """

    class Meta(UserSerializer.Meta):
        model = MyUser
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "first_enter",
        )
        read_only_fields = (
            "id",
            "email",
            "username",
        )
