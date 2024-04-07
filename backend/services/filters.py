import django_filters
from django_filters import rest_framework as filters

from .models import Services


class ServicesFilter(filters.FilterSet):
    """
    Фильтрация для модели Services.
    Attributes:
        name (CharFilter): Фильтр по имени сервиса (содержит).
        category (CharFilter): Фильтр по названию категории (содержит).
        is_popular (BooleanFilter): Фильтр по популярности.
    """

    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    category = django_filters.CharFilter(field_name="category__name", lookup_expr="icontains")
    is_popular = django_filters.BooleanFilter(field_name="is_popular",)

    class Meta:
        model = Services
        fields = (
            "name",
            "category",
            "is_popular",
        )
