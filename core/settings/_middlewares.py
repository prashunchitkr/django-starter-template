from core.settings._defaults import Defaults as D


class MiddlewareSettings:
    MIDDLEWARE = (
        D.MIDDLEWARE
        + [
            "core.middlewares.logging.RequestLoggingMiddleware",
        ]
    )
