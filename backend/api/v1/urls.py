from django.urls import include, path
from faqs.views import FaqViewSet
from payments.views import CashbackViewSet, PaymentMethodsViewSet, SubscriptionPaymentViewSet
from rest_framework import routers
from services.views import CategoriesViewSetViewSet, ServicesViewSet, SubscriptionServiceViewSet
from users.views import CustomUserViewSet

app_name = "api.v1"


router = routers.DefaultRouter()

router.register(r"users", CustomUserViewSet, "users")
router.register(r"categories", CategoriesViewSetViewSet, basename="categories")
router.register(r"services", ServicesViewSet, basename="services")
router.register(r"subscriptions", SubscriptionServiceViewSet, basename="subscriptions")
router.register(r"subscriptionspayment", SubscriptionPaymentViewSet,
                basename="subscriptionspayment")
router.register(r"paymentmethods", PaymentMethodsViewSet, basename="paymentmethods")
router.register(r"cashback", CashbackViewSet, basename=" cashback")
router.register(r"faqs", FaqViewSet, basename="faqs")


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
