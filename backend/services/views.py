from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Services, Subscription
from .serializers import ServicesSerializer, UserSubscriptionServiceSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (AllowAny,)
    pagination_class = LimitOffsetPagination

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: "Подписка добавлена.",
        }
    )
    @action(detail=True, methods=["post"], permission_classes=(IsAuthenticated,))
    def add(self, request, **kwargs):
        """
        Добавить новую подписку пользователю.
        """
        user = self.request.user
        services = get_object_or_404(Services, **kwargs)
        subscription = services.subscribe(user)
        serializer = UserSubscriptionServiceSerializer(
            subscription, context={"services": services}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: "Подписка удалена.",
        }
    )
    @action(detail=True, methods=["post"], permission_classes=(IsAuthenticated,))
    def disable(self, request, **kwargs):
        """
        Отписать пользователя от участия в данном курсе.

        Примечание:
            Это действие требует аутентификации пользователя и соответствующих прав.

        """
        user = self.request.user
        service = get_object_or_404(Services, **kwargs)
        subscription = get_object_or_404(
            Subscription,
            user=user,
            service=service,
            status=Subscription.Status.SUBSCRIBED,
        )
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
