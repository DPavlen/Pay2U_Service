from payments.models import Cashback, PaymentHistory
from rest_framework import serializers


class PaymentHistorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для истории оплаты подписки.
    """

    class Meta:
        model = PaymentHistory
        fields = (
            "id",
            "user",
            "subscription",
            "payment_method",
            "amount",
            "date",
            "status",
        )
        # read_only_fields = ("__all__",)


class CashbackSerializer(serializers.ModelSerializer):
    """
    Сериализатор для  получения кэшбека.
    """

    class Meta:
        model = Cashback
        fields = (
            "id",
            "subscription_service",
            "payment",
            "amount",
            "type_cashback",
            "status",
            "description",
        )
