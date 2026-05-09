import time
import traceback

import structlog

logger = structlog.get_logger(__name__)


class LoggingMixin:
    def get_log_data(self, request, response, **kwargs):
        return {}

    def dispatch(self, request, *args, **kwargs):
        start = time.monotonic()
        try:
            response = super().dispatch(request, *args, **kwargs)
            duration_ms = (time.monotonic() - start) * 1000
            log_data = {
                "view": self.__class__.__name__,
                "method": request.method,
                "path": request.path,
                "status_code": response.status_code,
                "duration_ms": round(duration_ms, 2),
            }
            if request.user.is_authenticated:
                log_data["user_id"] = str(request.user.pk)
            log_data.update(self.get_log_data(request, response, **kwargs))
            logger.info("view", **log_data)
            return response

        except Exception as exc:
            duration_ms = (time.monotonic() - start) * 1000
            log_data = {
                "view": self.__class__.__name__,
                "method": request.method,
                "path": request.path,
                "duration_ms": round(duration_ms, 2),
                "error": True,
                "exception": "".join(
                    traceback.format_exception(type(exc), exc, exc.__traceback__)
                ),
            }
            if request.user.is_authenticated:
                log_data["user_id"] = str(request.user.pk)
            logger.error("view", **log_data)
            raise
