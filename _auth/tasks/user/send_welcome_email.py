import structlog
from celery import shared_task

logger = structlog.get_logger(__name__)


@shared_task
def send_welcome_email(user_id):
    from _auth.models import User

    user = User.objects.get(pk=user_id)
    logger.info(
        "job",
        subject="send_welcome_email",
        user_id=str(user.pk),
        email=user.email,
    )
    return {"sent": True, "user_id": str(user.pk), "email": user.email}
