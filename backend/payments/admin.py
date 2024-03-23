from django.contrib import admin

from .models import Cashback, PaymentHistory


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
