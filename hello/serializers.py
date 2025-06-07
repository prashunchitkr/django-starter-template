from rest_framework import serializers


class GetHelloSerializer(serializers.Serializer):

    message = serializers.CharField(
        read_only=True,
    )
