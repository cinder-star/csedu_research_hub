from pytz import utc, timezone
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(
        self,
        email,
        password,
        full_name,
        **extra_fields
    ):
        if not email:
            raise ValueError("Users must have an email address")
        utc_now = utc.localize(datetime.utcnow())
        now = utc_now.astimezone(timezone("Asia/Dhaka"))
        user = self.model(
            email=email,
            full_name=full_name,
            last_login=now,
            is_active=True,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email=None, password=None, full_name=None, **extra_fields
    ):
        return self._create_user(
            email, password, full_name, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(
            email, password, **extra_fields
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = "auth_user"

    email = models.EmailField(_("Email Address"), primary_key=True)
    registration_number = models.IntegerField(unique=True, null=False)
    full_name = models.CharField(
        _("Full Name"),
        max_length=100,
        blank=False,
        null=False,
        unique=False,
        default=None,
    )
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    other = models.Manager()

    def __str__(self):
        return "email: {}\n".format(
            self.email
        )

    def get_email(self):
        return self.email