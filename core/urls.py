from django.conf import settings as S
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
]

if S.ENVIRONMENT.lower() in ("development",):
    urlpatterns += [
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
