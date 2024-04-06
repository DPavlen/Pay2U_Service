from payments.models import PaymentMethods, ServiceCashback, SubscriptionPayment, UserCashback
from rest_framework import serializers
from services.serializers import UserSubscriptionServiceSerializer
from users.serializers import ShortUserSerializer


class PaymentMethodsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для способов оплаты подписок.
    """

    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = PaymentMethods
        fields = (
            "id",
            "user",
            "payment_method",
            "icon",
        )


class SubscriptionPaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для связи между подпиской и оплатой.
    """

    subscription = UserSubscriptionServiceSerializer()
    payment_methods = PaymentMethodsSerializer()

    class Meta:
        model = SubscriptionPayment
        fields = (
            "id",
            "subscription",
            "payment_methods",
            "cost",
            "date",
            "expired_date",
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
            "service_cashback",
            "type_cashback",
            "amount_cashback",
        )


class UserCashbackSerializer(serializers.ModelSerializer):
    """
    Сериализатор для кэшбэка пользователя.
    """

    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = UserCashback
        fields = (
            "id",
            "tariff_cashback",
            "user",
            "subscription_payment",
            "description",
            "amount",
            "status",
        )
