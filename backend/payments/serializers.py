from payments.models import Cashback, PaymentMethods, SubscriptionPayment
from rest_framework import serializers


class PaymentMethodsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для истории оплаты подписки.
    """

    class Meta:
        model = PaymentMethods
        fields = (
            "id",
            "user",
            "subscription",
            "payment_method",
        )
        # read_only_fields = ("__all__",)


class SubscriptionPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPayment
        fields = (
            "id",
            "subscription",
            "payment_methods",
            "cost",
            "date",
            "status",


        )

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
            "payment_methods",
            "description",
            "amount",
            "type_cashback",
            "status",
        )
