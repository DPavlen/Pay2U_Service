from django.contrib.auth import authenticate
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

    def validate(self, data):
        """
        Пользовательская валидация данных.
        """
        request = self.context.get('request')
        if request and 'HTTP_AUTHORIZATION' in request.META:
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]  # Получение токена из заголовка Authorization
            user = authenticate(request=request, token=token)  # Попытка аутентификации пользователя по токену
            if user is not None:
                return data  # Если пользователь аутентифицирован успешно, возвращаем данные
            else:
                raise serializers.ValidationError("Invalid token")  # Если токен недействителен, вызываем ошибку
        else:
            raise serializers.ValidationError("Token not provided")  # Если токен не предоставлен, вызываем ошибку


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
    UserSerializer используется для просмотра.
    И обновления данных существующего пользователя.
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
