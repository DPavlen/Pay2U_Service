from django.contrib import admin

from .models import PaymentMethods, ServiceCashback, SubscriptionPayment, UserCashback


@admin.register(PaymentMethods)
class PaymentMethodsAdmin(admin.ModelAdmin):
    """
    Администратор методов оплаты.
    Отображает и фильтрует список методов оплаты.
    Attributes:
        - list_display: Список отображаемых полей в списке объектов.
        - list_filter: Список полей, по которым доступна фильтрация.
        - search_fields: Поля, по которым доступен поиск.
    """

    list_display = (
        "id",
        "user",
        "payment_method",
    )
    list_filter = ("id", "payment_method", "user",)
    search_fields = ("id", "user__username", "subscription__name")

    def get_queryset(self, request):
        """Получение запроса, учитывая права текущего пользователя."""
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset


@admin.register(SubscriptionPayment)
class SubscriptionPaymentAdmin(admin.ModelAdmin):
    """
    Администратор платежей за подписки.
    Отображает и фильтрует список платежей за подписки.
    Attributes:
        - list_display: Список отображаемых полей в списке объектов.
        - list_filter: Список полей, по которым доступна фильтрация.
        - search_fields: Поля, по которым доступен поиск.
    """

    list_display = (
        "id",
        "subscription",
        "payment_methods",
        "cost",
        "status",
        "expired_date",
    )
    list_filter = ("subscription", "payment_methods", "status", "expired_date")
    search_fields = ("subscription__id", "payment_methods", "status", "expired_date")

    def get_queryset(self, request):
        """
        Получение запроса, учитывая права текущего пользователя.
        """
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(user=request.user)


@admin.register(ServiceCashback)
class ServiceCashbackAdmin(admin.ModelAdmin):
    """
    Администратор кэшбека за услуги.
    Отображает и фильтрует список кэшбека за услуги.
    Attributes:
        - list_display: Список отображаемых полей в списке объектов.
        - list_filter: Список полей, по которым доступна фильтрация.
        - search_fields: Поля, по которым доступен поиск.
    """

    list_display = (
        "service_cashback",
        "type_cashback",
        "amount_cashback"
    )
    list_filter = ("service_cashback", "type_cashback", "amount_cashback")
    search_fields = ("service_cashback", "type_cashback", "amount_cashback")


@admin.register(UserCashback)
class UserCashbackAdmin(admin.ModelAdmin):
    """
    Администратор кэшбека пользователей.
    Отображает и фильтрует список кэшбека пользователей.
    Attributes:
        - list_display: Список отображаемых полей в списке объектов.
        - list_filter: Список полей, по которым доступна фильтрация.
        - search_fields: Поля, по которым доступен поиск.
    """

    list_display = (
        "tariff_cashback",
        "user",
        "subscription_payment",
        "description",
        "amount",
        "status"
    )
    list_filter = ("tariff_cashback", "user", "status")
    search_fields = ("tariff_cashback", "user", "status")
