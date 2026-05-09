import logging
import os
from pathlib import Path

import structlog
import uvicorn.config

uvicorn.config.LOGGING_CONFIG = {}


class DenyLoggersFilter(logging.Filter):
    def __init__(self, names):
        self.names = names

    def filter(self, record):
        return not any(record.name.startswith(n) for n in self.names)


structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)


_foreign_pre_chain = [
    structlog.contextvars.merge_contextvars,
    structlog.stdlib.add_logger_name,
    structlog.stdlib.add_log_level,
    structlog.processors.TimeStamper(fmt="iso"),
]


def _resolve_prod_log_path():
    path = Path(os.getenv("LOG_DIR", "./logs")) / "app.log"
    path.parent.mkdir(parents=True, exist_ok=True)
    return str(path)


def _make_console_renderer(colors=True):
    renderer = structlog.dev.ConsoleRenderer(colors=colors, sort_keys=False, pad_event_to=0)
    col_map = {c.key: c for c in renderer._columns}
    view_fmt = structlog.dev.KeyValueColumnFormatter(
        key_style=None,
        value_style=renderer._styles.bright + renderer._styles.logger_name,
        reset_style=renderer._styles.reset,
        value_repr=str,
        prefix="[",
        postfix="]",
    )
    renderer._columns = [
        col_map["timestamp"],
        col_map["level"],
        col_map["logger"],
        structlog.dev.Column("view", view_fmt),
        col_map["event"],
    ]
    return renderer


class DevelopmentLogging:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": _make_console_renderer(colors=True),
                "foreign_pre_chain": _foreign_pre_chain,
            },
        },
        "filters": {
            "deny": {
                "()": DenyLoggersFilter,
                "names": ("django.request", "uvicorn.access"),
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "console",
                "filters": ["deny"],
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
            "django.request": {
                "handlers": ["console"],
                "level": "ERROR",
                "propagate": False,
            },
            "django.server": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
            "uvicorn": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
            "uvicorn.error": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["console"],
                "level": "WARNING",
                "propagate": False,
            },
            "": {
                "handlers": ["console"],
                "level": "DEBUG",
            },
        },
    }


class ProductionLogging:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(),
                "foreign_pre_chain": _foreign_pre_chain,
            },
        },
        "filters": {
            "deny": {
                "()": DenyLoggersFilter,
                "names": ("django.request", "django.server", "uvicorn.access"),
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "json",
                "filters": ["deny"],
            },
            "file": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": _resolve_prod_log_path(),
                "when": "midnight",
                "backupCount": 30,
                "formatter": "json",
                "filters": ["deny"],
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console", "file"],
                "level": "INFO",
                "propagate": False,
            },
            "django.request": {
                "handlers": ["console", "file"],
                "level": "ERROR",
                "propagate": False,
            },
            "django.db.backends": {
                "handlers": ["console", "file"],
                "level": "WARNING",
                "propagate": False,
            },
            "django.server": {
                "handlers": ["console", "file"],
                "level": "ERROR",
                "propagate": False,
            },
            "uvicorn": {
                "handlers": ["console", "file"],
                "level": "INFO",
                "propagate": False,
            },
            "uvicorn.error": {
                "handlers": ["console", "file"],
                "level": "INFO",
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["console", "file"],
                "level": "WARNING",
                "propagate": False,
            },
            "": {
                "handlers": ["console", "file"],
                "level": "INFO",
            },
        },
    }
