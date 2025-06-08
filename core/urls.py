from django.conf import settings as S
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = []

if S.ENVIRONMENT.lower() in ("development",):
    urlpatterns += [
        path(
            "admin/",
            admin.site.urls,
        ),
        path(
            "swagger/schema/",
            SpectacularAPIView.as_view(),
            name="api_schema",
        ),
        path(
            "swagger/",
            SpectacularSwaggerView.as_view(url_name="api_schema"),
            name="api_swagger",
        ),
    ]

urlpatterns += [
    path(
        "",
        include("health.urls"),
    ),
    path(
        "auth/",
        include("_auth.urls"),
    ),
]
