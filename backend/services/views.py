from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
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
    """Класс для управления категориями."""

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
        Показать все сервисаы категории .
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
        operation_description="передай в query_params duration--> 1,3,6,12"
    )
    @action(detail=True, methods=["post"], permission_classes=(IsAuthenticated,))
    def add(self, request, **kwargs):
        """
        Добавить новую подписку пользователю.
        """
        user = self.request.user
        duration = self.request.query_params.get('duration')
        tariff = get_object_or_404(TariffList, services=get_object_or_404(
            Services, **kwargs), services_duration=duration
            )
        subscription = tariff.subscribe(user)
        subscription.check_subscription()
        serializer = UserSubscriptionServiceSerializer(
            subscription, context={"tariff": tariff}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "Подписка удалена.",
        }
    )
    @action(detail=True, methods=["post"], permission_classes=(IsAuthenticated,))
    def disable(self, request, **kwargs):
        """
        Отключить подписку.
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
        """
        try:
            tariff = TariffList.objects.filter(
                services=Services.objects.get(id=kwargs.get("pk"))
            )
        except TariffList.DoesNotExist:
            raise Http404
        serializer = ShortTariffListSerializer(tariff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubscriptionServiceViewSet(viewsets.ModelViewSet):
    """
    Класс для управления Подписками пользователей.
    """

    queryset = Subscription.objects.all()
    serializer_class = UserSubscriptionServiceSerializer
    permission_classes = (AllowAny,)
    pagination_class = LimitOffsetPagination

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Формирование календаря оплат.",
        }
    )
    @action(detail=False, methods=["get"], permission_classes=(IsAuthenticated,))
    def check_payments(self, request, **kwargs):
        """
        Формирование календаря оплат.
        """
        date_payment = {}
        subscriptions = request.user.subscriptions.all()
        for tariff in subscriptions:
            date_payment.setdefault(tariff.tariff.services.name,
                                    {"date": tariff.check_subscription(),
                                     "cost": tariff.tariff.tariff_full_price
                                     })
        return Response(date_payment, status=status.HTTP_200_OK)
