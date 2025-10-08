from django.urls import path
from _auth.views.user import ListUserView

urlpatterns = [
    path(
        "list/",
        ListUserView.as_view(),
        name="list_users",
    ),
]
