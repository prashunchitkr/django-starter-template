from rest_framework import serializers

from _auth.serializers import UserSerializer


class AuthHealthCheckResponseSerializer(serializers.Serializer):

    status = serializers.CharField()

    headers = serializers.DictField()

    user = UserSerializer(read_only=True)
