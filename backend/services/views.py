from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from payments.models import PaymentMethods, SubscriptionPayment
from payments.serializers import SubscriptionPaymentSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .filters import ServicesFilter
from .models import Category, Services, Subscription, TariffList
from .serializers import (  # TariffListSerializer,
    CategorySerializer,
    ServicesSerializer,
    ShortTariffListSerializer,
    UserSubscriptionServiceSerializer,
)


class CategoriesViewSetViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления категориями.
    Attributes:
        - queryset: Запрос для получения всех категорий.
        - serializer_class: Сериализатор категорий.
        - permission_classes: Классы разрешений для доступа к данным категорий.
        - pagination_class: Класс пагинации.
    Methods:
        - services(self, request, **kwargs): Метод для получения всех сервисов категории.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    pagination_class = LimitOffsetPagination

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Показать все сервисы категории.",
        }
    )
    @action(detail=True, methods=["get"], permission_classes=(IsAuthenticated,))
    def services(self, request, **kwargs):

        """
        Показать все сервисы категории.
        Parameters:
            request: Запрос.
            **kwargs: Дополнительные аргументы.
        Returns:
            Response: Ответ с данными сервисов категории.
        """

        try:
            services = Services.objects.filter(
                category=Category.objects.get(id=kwargs.get("pk"))
            )
        except Category.DoesNotExist:
            raise Http404
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServicesViewSet(viewsets.ModelViewSet):
    """
    Класс для управления сервисами.
    Attributes:
        - queryset: Запрос для получения всех сервисов.
        - serializer_class: Сериализатор сервисов.
        - permission_classes: Классы разрешений для доступа к данным сервисов.
        - filter_backends: Методы фильтрации данных.
        - filterset_class: Класс для фильтрации данных.
        - filterset_fields: Поля для фильтрации.
        - pagination_class: Класс пагинации.

    Methods:
        - add(self, request, **kwargs): Метод для добавления новой подписки пользователю.
        - disable(self, request, **kwargs): Метод для отключения подписки.
        - tariff(self, request, **kwargs): Метод для получения всех тарифов сервиса.
        - popular(self, request, **kwargs): Метод для получения популярных сервисов.
    """

    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ServicesFilter
    filterset_fields = ("name", "category__name", "is_popular")
    pagination_class = LimitOffsetPagination

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: "Подписка добавлена.",
        },
        query_serializer=None,
        operation_description="передай в headers duration--> 1,3,6,12"
    )
    @action(detail=True, methods=["post"], permission_classes=(IsAuthenticated,))
    def add(self, request, **kwargs):

        """
        Добавить новую подписку пользователю.
        Parameters:
            request: Запрос.
            **kwargs: Дополнительные аргументы.
        Returns:
            Response: Ответ с данными новой подписки.
        """

        user = self.request.user
        payment_methods = get_object_or_404(PaymentMethods, id=request.data.get("payment_methods"))
        auto_payment = request.data.get("auto_payment")
        duration = request.data.get("tariff_id")
        tariff = get_object_or_404(TariffList, services=get_object_or_404(
            Services, **kwargs), id=duration
            )
        subscription = tariff.subscribe(user, auto_payment)
        subs_pay = SubscriptionPayment.objects.create(
            subscription=subscription,
            cost=(tariff.tariff_promo_price if tariff.tariff_promo_price is not None else tariff.tariff_full_price) ,
            expired_date=subscription.check_subscription(),
            payment_methods=payment_methods,
            status="payment_completed",
        )
        serializer = SubscriptionPaymentSerializer(subs_pay)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "Подписка удалена.",
        }
    )
    @action(detail=True, methods=["post"], permission_classes=(IsAuthenticated,))
    def disable(self, request, **kwargs):

        """
        Отключить подписку.
        Parameters:
            request: Запрос.
            **kwargs: Дополнительные аргументы.
        Returns:
            Response: Ответ об успешном отключении подписки.
        """
        user = self.request.user
        tariff = get_object_or_404(TariffList, services=get_object_or_404(
            Services, **kwargs), subscriptions__user=self.request.user
            )
        subscription = get_object_or_404(
            Subscription,
            user=user,
            tariff=tariff,
            is_active=True,
        )
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Получить тарифные планы.",
        }
    )
    @action(detail=True, methods=["get"], permission_classes=(IsAuthenticated,))
    def tariff(self, request, **kwargs):
        """
        Показать все тарифы сервиса.
        Parameters:
            request: Запрос.
            **kwargs: Дополнительные аргументы.
        Returns:
            Response: Ответ с данными тарифов сервиса.
        """
        try:
            tariff = TariffList.objects.filter(
                services=Services.objects.get(id=kwargs.get("pk"))
            )
        except TariffList.DoesNotExist:
            raise Http404
        serializer = ShortTariffListSerializer(tariff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Получить популярные сервисы.",
        }
    )
    @action(detail=False, methods=["get"], permission_classes=(IsAuthenticated,))
    def popular(self, request, **kwargs):
        """
        Показать все популярные сервисы у которых is_popular=True.
        Parameters:
            request: Запрос.
            **kwargs: Дополнительные аргументы.
        Returns:
            Response: Ответ с данными популярных сервисов.
        """
        popular_services = self.queryset.filter(is_popular=True)[:20]
        serializer = self.get_serializer(popular_services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubscriptionServiceViewSet(viewsets.ModelViewSet):
    """
    Класс для управления Подписками пользователей.
    Attributes:
        queryset (Queryset): Запрос для получения списка подписок.
        serializer_class (Serializer): Класс сериализатора подписок.
        permission_classes (tuple): Кортеж классов разрешений.
        pagination_class (Pagination): Класс пагинации для списка подписок.
    """

    queryset = Subscription.objects.all()
    serializer_class = UserSubscriptionServiceSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        """
        Получение списка подписок пользователя.
        Returns:
        Queryset: Список подписок текущего пользователя.
        """
        return self.request.user.subscriptions.all()

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Формирование календаря оплат.",
        }
    )
    @action(detail=False, methods=["get"], permission_classes=(IsAuthenticated,))
    def check_payments(self, request, **kwargs):
        """
        Формирование календаря оплат.
        Parameters:
            request (HttpRequest): Запрос.
            **kwargs: Дополнительные аргументы.
        Returns:
            Response: Ответ с календарем оплат.
        """
        date_payment = {}
        subscriptions = request.user.subscriptions.all()
        for tariff in subscriptions:
            date_payment.setdefault(tariff.tariff.services.name,
                                    {"date": tariff.check_subscription(),
                                     "cost": tariff.tariff.tariff_full_price
                                     })
        return Response(date_payment, status=status.HTTP_200_OK)
