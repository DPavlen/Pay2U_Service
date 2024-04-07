from payments.models import PaymentMethods, ServiceCashback, SubscriptionPayment, UserCashback
from rest_framework import serializers
from services.serializers import UserSubscriptionServiceSerializer
from users.serializers import ShortUserSerializer


class PaymentMethodsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для способов оплаты подписок.
    Attributes:
        - user: Пользователь, связанный с способом оплаты.
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
    Attributes:
        - subscription: Информация о подписке, связанной с платежом.
        - payment_methods: Информация о методе оплаты подписки.
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
    Сериализатор для модели кэшбэка сервиса.
    Attributes:
        - service_cashback: Информация о сервисе, связанном с кэшбэком.
        - type_cashback: Тип кэшбэка.
        - amount_cashback: Количество кэшбэка.
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
    Сериализатор для модели кэшбэка пользователя.

    Attributes:
        - tariff_cashback: Тариф сервиса, связанный с кэшбэком пользователя.
        - user: Информация о пользователе, связанном с кэшбэком.
        - subscription_payment: Информация о платеже подписки, связанном с кэшбэком.
        - description: Описание кэшбэка.
        - amount: Количество кэшбэка.
        - status: Статус получения кэшбэка.
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
