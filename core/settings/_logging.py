class DevelopmentLogging:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "[{asctime}s] PID: {process:d} [{levelname}s] {message}s",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": True,
                "formatter": "verbose",
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": "INFO",
            },
        },
    }


class ProductionLogging:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "format": "{asctime}{levelname}{name}{message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "json",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": "INFO",
            },
            "django.request": {
                "handlers": ["console"],
                "level": "ERROR",
                "propagate": False,
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": "WARNING",
            },
        },
    }
