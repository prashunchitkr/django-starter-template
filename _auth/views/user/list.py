from rest_framework.generics import ListAPIView

from _auth.models.user import User
from _auth.serializers import ListUserSerializer


class ListUserView(ListAPIView):
    serializer_class = ListUserSerializer

    queryset = User.objects.order_by(
        "-created_at",
        "first_name",
        "last_name",
    )
