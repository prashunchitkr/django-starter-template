from django.db.models.signals import post_save
from django.dispatch import receiver

from _auth.models import User
from _auth.tasks import send_welcome_email


@receiver(post_save, sender=User)
def on_user_created(sender, instance, created, **kwargs):
    if created:
        send_welcome_email.delay(str(instance.pk))
