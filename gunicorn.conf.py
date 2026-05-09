import os

workers = int(os.getenv("GUNICORN_WORKERS", "4"))
threads = int(os.getenv("GUNICORN_THREADS", "2"))
timeout = int(os.getenv("GUNICORN_TIMEOUT", "120"))
bind = os.getenv("GUNICORN_BIND", "0.0.0.0:8000")

access_log_format = (
    "%({x-forwarded-for}i)s %({x-real-ip}i)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(D)s"  # noqa: E501
)
accesslog = "-"
errorlog = "-"
