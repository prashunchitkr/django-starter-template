from configurations.values import BooleanValue, Value

from core.settings._base import BaseSettings
from core.settings._django_spectacular import DjangoSpectacularSettings
from core.settings._logging import ProductionLogging


class ProductionSettings(
    DjangoSpectacularSettings,
    ProductionLogging,
    BaseSettings,
):
    DEBUG = BooleanValue(default=False)

    SECURE_SSL_REDIRECT = Value(default=True)

    SECURE_HSTS_SECONDS = Value(default=31536000)

    SECURE_HSTS_INCLUDE_SUBDOMAINS = Value(default=True)

    SECURE_HSTS_PRELOAD = Value(default=True)

    SESSION_COOKIE_SECURE = Value(default=True)

    CSRF_COOKIE_SECURE = Value(default=True)

    SECURE_CONTENT_TYPE_NOSNIFF = Value(default=True)

    SECURE_BROWSER_XSS_FILTER = Value(default=True)
