from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.accounts.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "name", "password")}),
        (
            "Permissions",
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
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "email",
        "name",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
        "last_login",
        "has_usable_password",
    )

    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    search_fields = ("email", "name")
    ordering = ("email", "-date_joined")
    date_hierarchy = "date_joined"
    filter_horizontal = ("groups", "user_permissions")

    actions = [
        "activate",
        "deactivate",
        "set_unusable_password",
    ]
