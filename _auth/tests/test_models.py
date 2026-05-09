import pytest

from _auth.models import User


class TestUserModel:
    def test_create_user(self, db):
        user = User.objects.create_user(
            email="test@example.com",
            password="testpass123",
            first_name="Test",
            last_name="User",
        )
        assert user.email == "test@example.com"
        assert user.first_name == "Test"
        assert user.last_name == "User"
        assert not user.is_staff
        assert not user.is_superuser
        assert user.is_active
        assert user.pk is not None

    def test_create_user_without_email(self, db):
        with pytest.raises(ValueError, match="The given email must be set"):
            User.objects.create_user(email="", password="testpass123")

    def test_create_superuser(self, db):
        user = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpass123",
        )
        assert user.email == "admin@example.com"
        assert user.is_staff
        assert user.is_superuser

    def test_email_uniqueness(self, db):
        User.objects.create_user(email="unique@example.com", password="testpass123")
        with pytest.raises(Exception):  # noqa: B017
            User.objects.create_user(email="unique@example.com", password="testpass456")

    def test_str_representation(self, db):
        user = User.objects.create_user(email="str@example.com", password="testpass123")
        assert str(user) == "str@example.com"

    def test_user_ordering(self, db):
        User.objects.create_user(email="b@example.com", password="testpass123")
        User.objects.create_user(email="a@example.com", password="testpass123")
        users = User.objects.all()
        assert list(users) == list(users.order_by("-created_at"))
