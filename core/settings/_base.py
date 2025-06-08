from configurations import Configuration
from dotenv import load_dotenv

from core.settings._apps import AppsSettings
from core.settings._cache import CacheSettings
from core.settings._cors import CorsSettings
from core.settings._database import DatabaseSettings
from core.settings._i18n import I18NSettings
from core.settings._jwt import JWTSettings
from core.settings._middlewares import MiddlewareSettings
from core.settings._rest_framework import RestFrameworkSettings
from core.settings._security import SecuritySettings
from core.settings._static import StaticFilesSettings
from core.settings._templates import TemplateSettings
from core.settings._validators import ValidatorsSettings


class BaseSettings(
    JWTSettings,
    RestFrameworkSettings,
    TemplateSettings,
    CacheSettings,
    DatabaseSettings,
    CorsSettings,
    ValidatorsSettings,
    StaticFilesSettings,
    SecuritySettings,
    MiddlewareSettings,
    AppsSettings,
    I18NSettings,
    Configuration,
):

    load_dotenv()

    @classmethod
    def post_setup(cls):
        super(BaseSettings, cls).post_setup()
