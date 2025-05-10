from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _


class PermissionAdmin(admin.ModelAdmin):

    model = Permission

    fields = ("name",)


class UserAdmin(BaseUserAdmin):

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = (
        "id",
        "email",
        "is_staff",
        "is_superuser",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
    )
    ordering = (
        "date_joined",
        "email",
    )


admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Permission, PermissionAdmin)
