from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from health.serializers import HealthCheckResponseSerializer


class HealthCheckView(RetrieveAPIView):

    permission_classes = (AllowAny,)

    serializer_class = HealthCheckResponseSerializer

    def get_object(self):

        data = {
            "status": "OK",
            "headers": self.request.headers,
        }

        return data
