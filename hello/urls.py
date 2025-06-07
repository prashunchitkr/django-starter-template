from django.urls import path

from hello.views import GetHelloView

urlpatterns = [
    path(
        "",
        GetHelloView.as_view(),
        name="get_hello",
    )
]
