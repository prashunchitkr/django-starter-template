from core.settings._defaults import Defaults as D


class AppsSettings:

    INSTALLED_APPS = D.INSTALLED_APPS + [
        # User installed apps
        "_auth",
        "hello",
    ]
