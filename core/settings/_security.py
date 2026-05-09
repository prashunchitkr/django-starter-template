from configurations.values import SecretValue


class SecuritySettings:
    ENVIRONMENT = SecretValue()

    SECRET_KEY = SecretValue()

    ROOT_URLCONF = "core.urls"

    ASGI_APPLICATION = "core.asgi.application"

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    AUTH_USER_MODEL = "_auth.User"
