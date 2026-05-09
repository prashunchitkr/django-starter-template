from configurations.values import Value


class CelerySettings:
    CELERY_BROKER_URL = Value()

    CELERY_RESULT_BACKEND = Value()

    CELERY_ACCEPT_CONTENT = ["json"]

    CELERY_TASK_SERIALIZER = "json"

    CELERY_RESULT_SERIALIZER = "json"

    CELERY_TIMEZONE = "UTC"

    CELERY_TASK_TRACK_STARTED = True

    CELERY_TASK_TIME_LIMIT = 300

    CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
