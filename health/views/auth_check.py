from rest_framework.generics import RetrieveAPIView

from base.mixins import LoggingMixin
from health.serializers import AuthHealthCheckResponseSerializer


class AuthHealthCheckView(LoggingMixin, RetrieveAPIView):
    serializer_class = AuthHealthCheckResponseSerializer

    def get_object(self):
        return {
            "status": "OK",
            "user": self.request.user,
        }
