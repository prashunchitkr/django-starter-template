from rest_framework.generics import ListAPIView

from _auth.models.user import User
from _auth.serializers import ListUserSerializer
from base.mixins import LoggingMixin


class ListUserView(LoggingMixin, ListAPIView):
    serializer_class = ListUserSerializer

    queryset = User.objects.order_by(
        "-created_at",
        "first_name",
        "last_name",
    )

    def get_log_data(self, request, response, **kwargs):
        return {
            "total_users": self.get_queryset().count(),
            "returned_count": len(response.data.get("results", [])),
        }
