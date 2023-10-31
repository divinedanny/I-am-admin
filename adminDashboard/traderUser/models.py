from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# Create your models here.

class UserManger(BaseUserManager):
    def create_user(self, email, password, lastname, firstname, **other_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            lastname=lastname,
            firstname=firstname,
            **other_fields
        )
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, lastname, firstname, **other_fields):
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_admin", True)
        other_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, lastname, firstname, **other_fields)


class TraderUser(AbstractUser, PermissionsMixin):
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(_("username"), max_length=30, unique=True, null=False, blank=False)
    firstname = models.CharField(_("firstname"),max_length=50)
    lastname = models.CharField(_("lastname"),max_length=50)
    email = models.EmailField(_("emailaddress"), unique=True)
    is_active = models.BooleanField(_("is_active"), default=False)
    is_admin = models.BooleanField(_("is_staff"), default=False)
    date_joined = models.DateTimeField(_("date_joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("last_login"), auto_now=True)
    
    
    objects = UserManger()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname"]
    
    