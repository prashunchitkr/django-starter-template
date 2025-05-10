from configurations.values import SecretValue


class SecuritySettings:

    SECRET_KEY = SecretValue()

    ROOT_URLCONF = "core.urls"

    WSGI_APPLICATION = "core.wsgi.application"

    ASGI_APPLICATION = "core.asgi.application"

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    AUTH_USER_MODEL = "_auth.User"

    DATA_SIGN_KEY = SecretValue()
