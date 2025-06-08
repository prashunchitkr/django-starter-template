from rest_framework import serializers


class HealthCheckResponseSerializer(serializers.Serializer):

    status = serializers.CharField()

    headers = serializers.DictField()
