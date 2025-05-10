from core.settings._base import BaseSettings
from core.settings._logging import DevelopmentLogging


class DevelopmentSettings(
    DevelopmentLogging,
    BaseSettings,
):

    DEBUG = True
