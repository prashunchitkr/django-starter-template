from rest_framework.generics import RetrieveAPIView

from health.serializers import AuthHealthCheckResponseSerializer


class AuthHealthCheckView(RetrieveAPIView):
    serializer_class = AuthHealthCheckResponseSerializer

    def get_object(self):
        return {
            "status": "OK",
            "user": self.request.user,
        }
