from rest_framework import serializers

from _auth.models import User


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
        )
