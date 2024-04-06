# import datetime

import pytest


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(username="TestUser", password="1234567", email="test@test.com")


@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(username="TestUser2", password="1234567", email="test2@test.com")


@pytest.fixture
def token(user):
    from rest_framework_simplejwt.tokens import RefreshToken

    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(Authorization=f'Token {token["access"]}')
    return client


@pytest.fixture
def anonymous_client():
    from rest_framework.test import APIClient

    client = APIClient()
    return client
