from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "_auth"

    def ready(self):
        import _auth.signals.user.send_welcome_email  # noqa: F401
