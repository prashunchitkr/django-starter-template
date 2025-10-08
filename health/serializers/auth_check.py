from rest_framework import serializers

from _auth.serializers import ListUserSerializer


class AuthHealthCheckResponseSerializer(serializers.Serializer):
    status = serializers.CharField()

    headers = serializers.DictField()

    user = ListUserSerializer(read_only=True)
