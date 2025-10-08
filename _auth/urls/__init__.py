from django.urls import include, path
from _auth.urls import token, user


urlpatterns = [
    path("token/", include(token.urlpatterns)),
    path("user/", include(user.urlpatterns)),
]
