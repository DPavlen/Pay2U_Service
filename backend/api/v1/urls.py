from django.urls import include, path
from faqs.views import FaqViewSet
from payments.views import (
    PaymentMethodsViewSet,
    ServiceCashbackViewSet,
    SubscriptionPaymentViewSet,
    UserCashbackViewSet,
)
from rest_framework import routers
from services.views import CategoriesViewSetViewSet, ServicesViewSet, SubscriptionServiceViewSet
from users.views import CustomUserViewSet

app_name = "api.v1"


router = routers.DefaultRouter()

router.register(r"users", CustomUserViewSet, "users")
router.register(r"categories", CategoriesViewSetViewSet, basename="categories")
router.register(r"services", ServicesViewSet, basename="services")
router.register(r"subscriptions", SubscriptionServiceViewSet, basename="subscriptions")

router.register(r"payment_methods", PaymentMethodsViewSet, basename="payment_methods")
router.register(r"subscriptions_payment", SubscriptionPaymentViewSet,
                basename="subscriptions_payment")
router.register(r"service_cashback",
                ServiceCashbackViewSet, basename="service_cashback")
router.register(r"user_cashback",
                UserCashbackViewSet, basename="user_cashback")

router.register(r"faqs", FaqViewSet, basename="faqs")


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
