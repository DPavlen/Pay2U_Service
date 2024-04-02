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
    #    from djoser.views import TokenCreateView
    from djoser.utils import login_user

    refresh = login_user(user)

    return {
        "access": str(refresh),
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
