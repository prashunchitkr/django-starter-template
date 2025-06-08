from django.urls import path

from health.views import AuthHealthCheckView, HealthCheckView

urlpatterns = [
    path(
        "health/",
        HealthCheckView.as_view(),
        name="health_check",
    ),
    path(
        "health/auth/",
        AuthHealthCheckView.as_view(),
        name="auth_health_check",
    ),
]
