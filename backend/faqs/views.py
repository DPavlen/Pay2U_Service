from faqs.models import Faq
from faqs.serializers import FaqSerializer
from rest_framework import viewsets

# from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny


class FaqViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Основная View о списке часто задаваемых вопросов.
    Attributes:
        - queryset: Запрос, возвращающий все объекты PaymentHistory.
        - serializer_class: PaymentHistorySerializer
        - permission_classes: Пока всем
        - pagination_class: Стандартный класс пагинации.
    """

    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    permission_classes = (AllowAny,)
    # pagination_class = LimitOffsetPagination
