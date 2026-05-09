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

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    objects = UserManager()

    class Meta(AbstractUser.Meta, BaseModel.Meta):
        ordering = ("-created_at",)
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self) -> str:
        return self.email
