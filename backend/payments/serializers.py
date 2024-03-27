from payments.models import Cashback, PaymentHistory, SubscriptionPayment
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


class SubscriptionPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPayment
        fields = ['id', 'subscription', 'payment_history']

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['subscription'] = instance.subscription.service
    #     representation['payment_history'] = instance.payment_history.id
    #     return representation


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
