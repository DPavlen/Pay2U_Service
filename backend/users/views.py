from typing import Tuple

from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from users.models import MyUser
from users.serializers import CustomUserSerializer, UpdateUserSerializer


class CustomUserViewSet(UserViewSet):
    """
    Кастомный ViewSet для работы с пользователями.
    Он предоставляет эндпоинты для управления пользователями,
    включая активацию.
    Attributes:
        - queryset: Запрос, возвращающий все объекты User.
        - serializer_class: Сериализатор, используемый для преобразования
        данных пользователя.
    Permissions:
        - permission_classes: Список классов разрешений для ViewSet. Здесь
        установлен AllowAny для открытого доступа.
    Methods:
        - activate(self, request, uid, token, format=None): Активирует
        пользователя с заданным UID и токеном.
    """

    queryset = MyUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self) -> Tuple:
        """
        Возвращает соответствующий сериализатор в зависимости от действия.
        """
        if self.action == "list":
            return (IsAdminUser(),)
        return (AllowAny(),)

    @action(
        detail=False,
        methods=["get", "patch"],
        permission_classes=[IsAuthenticated],
    )
    @action(["get", "patch"], detail=False)
    def me(self, request):
        if request.method == "GET":
            user = request.user
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == "PATCH":
            user = request.user
            serializer = UpdateUserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
