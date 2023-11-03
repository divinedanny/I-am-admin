from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

# Create your models here.

class TraderUsers(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_an_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    
