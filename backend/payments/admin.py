from django.contrib import admin

from .models import Cashback, PaymentHistory, SubscriptionPayment


@admin.register(PaymentHistory)
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "subscription",
        "payment_method",
        "amount",
        "date",
        "status",
    )
    list_filter = ("payment_method", "date", "status")
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
        "payment",
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
        "payment_history",
    )
    list_filter = ("subscription", "payment_history")
    search_fields = ("subscription__id", "payment_history__id")
