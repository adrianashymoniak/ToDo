import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from apps.accounts.services import get_first_name, get_last_name, days_on_site


class UserManager(BaseUserManager):
    """
    Creates and saves a User with the given email, phone,
    password and optional extra info.
    """

    def _create_user(
        self, email, name, password, is_staff, is_superuser, is_active,
            **extra_fields,
    ):
        """
        Creates and saves a User with the given username, email and password
        """
        now = timezone.now()

        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name or "",
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            date_joined=now,
            last_login=now,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name=None, password=None, **extra_fields):
        kwargs = {
            "email": email,
            "name": name,
            "password": password,
            "is_staff": False,
            "is_active": False,
            "is_superuser": False,
        }
        kwargs.update(extra_fields)
        return self._create_user(**kwargs)

    def create_superuser(self, email, name=None, password=None,
                         **extra_fields,):
        """
        Creates and saves a superuser with the given email, phone and password.
        """
        kwargs = {
            "email": email,
            "name": name,
            "password": password,
            "is_staff": True,
            "is_active": True,
            "is_superuser": True,
        }
        kwargs.update(extra_fields)
        return self._create_user(**kwargs)

    def get_by_natural_key(self, email):
        return self.get(email__iexact=email)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email", max_length=255, unique=True)
    name = models.CharField("Full name", max_length=255, default="Test User")

    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
                  "Unselect this instead of deleting accounts.",
    )

    date_joined = models.DateTimeField("Date joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"

    @property
    def first_name(self) -> str:
        return get_first_name(self)

    @property
    def last_name(self) -> str:
        return get_last_name(self)

    @property
    def days_on_site(self) -> datetime:
        return days_on_site(self)

    def has_usable_password(self) -> bool:
        return super().has_usable_password()

    has_usable_password.boolean = True

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["name", "-date_joined"]
