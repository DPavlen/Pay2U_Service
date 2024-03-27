from payments.models import Cashback, PaymentHistory, SubscriptionPayment
from payments.serializers import CashbackSerializer, PaymentHistorySerializer, SubscriptionPaymentSerializer
from rest_framework import viewsets

# from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny


class PaymentHistoryViewSet(viewsets.ModelViewSet):
    """
    Основная View об историях оплат подписок.
    Attributes:
        - queryset: Запрос, возвращающий все объекты PaymentHistory.
        - serializer_class: PaymentHistorySerializer
        - permission_classes: Пока всем
        - pagination_class: Стандартный класс пагинации.
    """

    queryset = PaymentHistory.objects.all()
    serializer_class = PaymentHistorySerializer
    permission_classes = (AllowAny,)
    # pagination_class = LimitOffsetPagination

    # def get_queryset(self):
    #     """Проверка Истории платежей по текущему user."""
    #     user = self.request.user
    #     return PaymentHistory.objects.filter(user=user)


class SubscriptionPaymentViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPayment.objects.all()
    serializer_class = SubscriptionPaymentSerializer


class CashbackViewSet(viewsets.ModelViewSet):
    """
    Основная View о получении кэшбека.
    Attributes:
        - queryset: Запрос, возвращающий все объекты PaymentHistory.
        - serializer_class: CashbackSerializer
        - permission_classes: Пока всем
        - pagination_class: Стандартный класс пагинации.
    """

    queryset = Cashback.objects.all()
    serializer_class = CashbackSerializer
    permission_classes = (AllowAny,)
    # pagination_class = LimitOffsetPagination
