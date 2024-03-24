from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FaqViewSet

router = DefaultRouter()
router.register(r"faqs", FaqViewSet, basename="faqs")


urlpatterns = [
    path("", include(router.urls)),
]
