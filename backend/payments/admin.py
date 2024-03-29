from django.contrib import admin

from .models import Cashback, PaymentMethods, SubscriptionPayment


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


@admin.register(Cashback)
class CashbackAdmin(admin.ModelAdmin):
    list_display = (
        "subscription_service",
        "payment_methods",
        "amount",
        "type_cashback",
        "status",
    )
    list_filter = ("type_cashback", "status")
    search_fields = ("subscription_service__name",)


@admin.register(SubscriptionPayment)
class SubscriptionPaymentAdmin(admin.ModelAdmin):
    list_display = (
        "subscription",
        "payment_methods",
    )
    list_filter = ("subscription", "payment_methods")
    search_fields = ("subscription__id", "payment_methods")
