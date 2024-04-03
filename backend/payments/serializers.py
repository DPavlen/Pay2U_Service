from payments.models import PaymentMethods, ServiceCashback, SubscriptionPayment, UserCashback
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


class ServiceCashbackSerializer(serializers.ModelSerializer):
    """
    Сериализатор для  сервиса кэшбека.
    """

    class Meta:
        model = ServiceCashback
        fields = (
            "id",
            "subscription_service",
            "type_cashback",
        )


class UserCashbackSerializer(serializers.ModelSerializer):
    """
    Сериализатор для кэшбэка пользователя.
    """

    class Meta:
        model = UserCashback
        fields = (
            "id",
            "service_cashback",
            "user",
            "subscription_payment",
            "description",
            "amount",
            "status",
        )
