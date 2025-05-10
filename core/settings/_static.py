from core.settings._defaults import Defaults as D


class StaticFilesSettings:

    STATIC_URL = "static/"

    STATIC_ROOT = D.BASE_DIR / "staticfiles"
