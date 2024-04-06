# import datetime

# import pytest
# from django.dispatch import receiver
# from django.urls import reverse
# from rest_framework import status
# from services.models import Category, Services, Subscription, TariffList

# from tests.factories.services import CategoryFactory, ServicesFactory
# from tests.factories.users import UserFactory


# @pytest.mark.django_db(transaction=True)
# class Testservices:
#     url = reverse("services")

#     def test_creation_of_services(self):
#         """Тест, что модель Services создается в БД."""
#         _ = CategoryFactory()
#         services = ServicesFactory()
#         obj = Services.objects.get(id=services.id)
#         assert obj == services

#     def test_not_found_serviceslist(self, user_client):
#         _ = ServicesFactory()
#         response = user_client.get(self.url)
#         assert response.status_code != status.HTTP_404_NOT_FOUND
#         assert response.status_code == status.HTTP_200_OK
