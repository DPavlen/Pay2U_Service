from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CashbackViewSet, PaymentMethodsViewSet

router = DefaultRouter()

router.register(r"paymentmethods", PaymentMethodsViewSet, basename="paymentmethods")
router.register(r" cashback", CashbackViewSet, basename=" cashback")


urlpatterns = [
    path("", include(router.urls)),
]
