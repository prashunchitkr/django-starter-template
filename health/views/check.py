from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from base.mixins import LoggingMixin
from health.serializers import HealthCheckResponseSerializer


class HealthCheckView(LoggingMixin, RetrieveAPIView):
    permission_classes = (AllowAny,)

    serializer_class = HealthCheckResponseSerializer

    def get_object(self):
        return {"status": "OK"}
