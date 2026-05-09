import os

import pytest
from rest_framework.test import APIClient

from _auth.models import User

os.environ.setdefault("DJANGO_CONFIGURATION", "TestingSettings")


@pytest.fixture
def user() -> User:
    return User.objects.create_user(
        email="test@example.com",
        password="testpass123",
        first_name="Test",
        last_name="User",
    )


@pytest.fixture
def superuser() -> User:
    return User.objects.create_superuser(
        email="admin@example.com",
        password="adminpass123",
        first_name="Admin",
        last_name="User",
    )


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def authenticated_client(api_client: APIClient, user: User) -> APIClient:
    from rest_framework_simplejwt.tokens import AccessToken

    token = AccessToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client
