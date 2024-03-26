from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CashbackViewSet, PaymentHistoryViewSet

router = DefaultRouter()

router.register(r"paymenthistory", PaymentHistoryViewSet, basename="paymenthistory")
router.register(r" cashback", CashbackViewSet, basename=" cashback")


urlpatterns = [
    path("", include(router.urls)),
]
