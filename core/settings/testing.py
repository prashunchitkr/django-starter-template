from configurations.values import BooleanValue

from core.settings._base import BaseSettings
from core.settings._logging import DevelopmentLogging


class TestingSettings(
    DevelopmentLogging,
    BaseSettings,
):
    DEBUG = BooleanValue(default=True)

    ALLOWED_HOSTS = ["*"]

    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        }
    }

    PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.MD5PasswordHasher",
    ]
