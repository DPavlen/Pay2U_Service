from django.contrib import admin

from .models import PaymentMethods, ServiceCashback, SubscriptionPayment, UserCashback


@admin.register(PaymentMethods)
class PaymentMethodsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "subscription",
        "payment_method",
    )
    list_filter = ("payment_method", "user", "subscription")
    search_fields = ("user__username", "subscription__name")

    def get_queryset(self, request):
        """Проверка на фильтрацию по текущему пользователю."""
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset


@admin.register(SubscriptionPayment)
class SubscriptionPaymentAdmin(admin.ModelAdmin):
    list_display = (
        "subscription",
        "payment_methods",
        "cost",
        "status"
    )
    list_filter = ("subscription", "payment_methods")
    search_fields = ("subscription__id", "payment_methods")


@admin.register(ServiceCashback)
class ServiceCashbackAdmin(admin.ModelAdmin):
    list_display = (
        "subscription_service",
        "type_cashback",
    )
    list_filter = ("subscription_service", "type_cashback")
    search_fields = ("subscription_service", "type_cashback")


@admin.register(UserCashback)
class UserCashbackAdmin(admin.ModelAdmin):
    list_display = (
        "service_cashback",
        "user",
        "subscription_payment",
        "description",
        "amount",
        "status"
    )
    list_filter = ("service_cashback", "user", "status")
    search_fields = ("service_cashback", "user", "status")
