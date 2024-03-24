from payments.models import Cashback, PaymentHistory
from payments.serializers import CashbackSerializer, PaymentHistorySerializer
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
