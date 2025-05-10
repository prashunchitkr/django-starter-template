from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from _auth.managers import UserManager
from base.models import BaseModel


class User(AbstractUser, BaseModel):

    username = None

    email = models.EmailField(
        _("email address"),
        unique=True,
        db_index=True,
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = (
        "first_name",
        "last_name",
    )

    objects = UserManager()
