from djoser.serializers import UserSerializer
from rest_framework import serializers
from users.models import MyUser


class CustomUserSerializer(UserSerializer):
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
        )
        extra_kwargs = {
            "email": {"required": False},
            "username": {"required": True},
            "first_name": {"required": False},
            "last_name": {"required": False},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = MyUser(
            email=validated_data["email"],
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
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
