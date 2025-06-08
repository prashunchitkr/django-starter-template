from rest_framework.generics import RetrieveAPIView

from health.serializers import AuthHealthCheckResponseSerializer


class AuthHealthCheckView(RetrieveAPIView):

    serializer_class = AuthHealthCheckResponseSerializer

    def get_object(self):

        data = {
            "status": "OK",
            "headers": self.request.headers,
            "user": self.request.user,
        }

        return data
