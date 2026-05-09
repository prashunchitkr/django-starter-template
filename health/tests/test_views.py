from django.urls import reverse
from rest_framework.test import APIClient


class TestHealthCheckView:
    url = reverse("health_check")

    def test_returns_ok(self, db, api_client):
        response = api_client.get(self.url)
        assert response.status_code == 200
        assert response.data["status"] == "OK"

    def test_requires_no_auth(self, db, api_client):
        response = api_client.get(self.url)
        assert response.status_code == 200


class TestAuthHealthCheckView:
    url = reverse("auth_health_check")

    def test_returns_ok_when_authenticated(self, db, authenticated_client: APIClient):
        response = authenticated_client.get(self.url)
        assert response.status_code == 200
        assert response.data["status"] == "OK"
        assert "user" in response.data

    def test_requires_authentication(self, db, api_client):
        response = api_client.get(self.url)
        assert response.status_code == 401

    def test_returns_user_details(self, db, authenticated_client, user):
        response = authenticated_client.get(self.url)
        assert response.data["user"]["email"] == user.email
