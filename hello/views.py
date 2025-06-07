from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from hello.serializers import GetHelloSerializer


class GetHelloView(RetrieveAPIView):

    permission_classes = (AllowAny,)

    serializer_class = GetHelloSerializer

    def get_object(self):
        return {
            "message": "Hello World",
        }
