from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from payments.models import PaymentMethods, ServiceCashback, SubscriptionPayment, UserCashback
from payments.serializers import (
    PaymentMethodsSerializer,
    ServiceCashbackSerializer,
    SubscriptionPaymentSerializer,
    UserCashbackSerializer,
)
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PaymentMethodsViewSet(viewsets.ModelViewSet):
    """
    Основная View о способах оплат пользователя.
    Attributes:
        - queryset: Запрос, возвращающий все объекты PaymentMethods.
        - serializer_class: PaymentMethodsSerializer
        - permission_classes: IsAuthenticated
        - pagination_class: Стандартный класс пагинации.
    """

    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        """Проверка способов оплат по текущему пользователю."""
        user = self.request.user
        return PaymentMethods.objects.filter(user=user)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK:
                "Получить по способам оплат текущего userа его оплаты/подписки .",
        }
    )
    @action(detail=True, methods=['get'])
    def subscription_payments(self, request, **kwargs):
        """
        Получить по способам оплат текущего userа его оплаты/подписки.
        """
        try:
            payment_method = self.get_object()
            subscription_payments = SubscriptionPayment.objects.filter(payment_methods=payment_method)
            subscription_payments_serializer = SubscriptionPaymentSerializer(
                subscription_payments, many=True
            )
            payment_method_serializer = PaymentMethodsSerializer(payment_method)
            response_data = {
                "payment_methods": payment_method_serializer.data,
                "subscription_payments": subscription_payments_serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except PaymentMethods.DoesNotExist:
            raise Http404


class SubscriptionPaymentViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPayment.objects.all()
    serializer_class = SubscriptionPaymentSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination


class ServiceCashbackViewSet(viewsets.ModelViewSet):
    """
    Основная View о кэшбэке сервиса.
    Attributes:
        - queryset: Запрос, возвращающий все объекты PaymentHistory.
        - serializer_class: ServiceCashbackSerializer
        - permission_classes: IsAuthenticated
        - pagination_class: Стандартный класс пагинации.
    """

    queryset = ServiceCashback.objects.all()
    serializer_class = ServiceCashbackSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination


class UserCashbackViewSet(viewsets.ModelViewSet):
    """
    Основная View о кэшбэке сервиса.
    Attributes:
        - queryset: Запрос, возвращающий все объекты UserCashback.
        - serializer_class: CUserCashbackSerializer
        - permission_classes: IsAuthenticated
        - pagination_class: Стандартный класс пагинации.
    """

    queryset = UserCashback.objects.all()
    serializer_class = UserCashbackSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        """Проверка кэшбека по текущему пользователю."""
        user = self.request.user
        return UserCashback.objects.filter(user=user)
