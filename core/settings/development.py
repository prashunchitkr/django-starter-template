from configurations.values import BooleanValue

from core.settings._base import BaseSettings
from core.settings._django_spectacular import DjangoSpectacularSettings
from core.settings._logging import DevelopmentLogging


class DevelopmentSettings(
    DjangoSpectacularSettings,
    DevelopmentLogging,
    BaseSettings,
):
    DEBUG = BooleanValue(default=True)
