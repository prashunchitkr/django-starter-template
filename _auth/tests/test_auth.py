from django.urls import reverse
from rest_framework.test import APIClient

from _auth.models.user import User


class TestTokenObtain:
    url = reverse("token_obtain_pair")

    def test_obtain_token_success(self, db, user: User, api_client: APIClient):
        response = api_client.post(
            self.url,
            {"email": user.email, "password": "testpass123"},
            format="json",
        )
        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data

    def test_obtain_token_invalid_credentials(self, db, api_client: APIClient):
        response = api_client.post(
            self.url,
            {"email": "wrong@example.com", "password": "wrongpass"},
            format="json",
        )
        assert response.status_code == 401

    def test_obtain_token_missing_fields(self, db, api_client: APIClient):
        response = api_client.post(self.url, {}, format="json")
        assert response.status_code == 400


class TestTokenRefresh:
    def test_refresh_token(self, db, user: User, api_client: APIClient):
        obtain_response = api_client.post(
            reverse("token_obtain_pair"),
            {"email": user.email, "password": "testpass123"},
            format="json",
        )
        refresh_token = obtain_response.data["refresh"]

        response = api_client.post(
            reverse("token_refresh"),
            {"refresh": refresh_token},
            format="json",
        )
        assert response.status_code == 200
        assert "access" in response.data
