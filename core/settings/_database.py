from core.settings._defaults import Defaults as D


class DatabaseSettings:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": D.BASE_DIR / "db.sqlite3",
        }
    }
