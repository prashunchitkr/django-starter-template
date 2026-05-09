from django.urls import reverse


class TestUserListView:
    url = reverse("list_users")

    def test_requires_authentication(self, db, api_client):
        response = api_client.get(self.url)
        assert response.status_code == 401

    def test_lists_users(self, db, authenticated_client, user):
        from _auth.models import User

        User.objects.create_user(
            email="another@example.com",
            password="testpass123",
            first_name="Another",
            last_name="User",
        )

        response = authenticated_client.get(self.url)
        assert response.status_code == 200
        assert response.data["count"] >= 2

    def test_returns_expected_fields(self, db, authenticated_client, user):
        response = authenticated_client.get(self.url)
        assert response.status_code == 200
        result = response.data["results"][0]
        assert "id" in result
        assert "email" in result
        assert "first_name" in result
        assert "last_name" in result
