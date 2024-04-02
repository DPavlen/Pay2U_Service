import factory.fuzzy
from payments.models import PaymentMethods

from .services import SubscriptionFactory
from .users import UserFactory


class PaymentMethodsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PaymentMethods

    user = factory.SubFactory(UserFactory)
    subscription = factory.SubFactory(SubscriptionFactory)
    payment_method = PaymentMethods.PaymentMethodChoises.SBP
