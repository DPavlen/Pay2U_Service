from payments.models import PaymentMethods, ServiceCashback, SubscriptionPayment, UserCashback
from payments.serializers import (
    PaymentMethodsSerializer,
    ServiceCashbackSerializer,
    SubscriptionPaymentSerializer,
    UserCashbackSerializer,
)
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


class PaymentMethodsViewSet(viewsets.ModelViewSet):
    """
    Основная View об историях оплат подписок.
    Attributes:
        - queryset: Запрос, возвращающий все объекты PaymentHistory.
        - serializer_class: PaymentHistorySerializer
        - permission_classes: Пока всем
        - pagination_class: Стандартный класс пагинации.
    """

    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    # def get_queryset(self):
    #     """Проверка Истории платежей по текущему user."""
    #     user = self.request.user
    #     return PaymentHistory.objects.filter(user=user)


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
