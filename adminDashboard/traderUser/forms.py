from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import TraderUser

class TraderUserForm(UserCreationForm):
    class Meta:
        model = TraderUser
        fields = ["username","firstname", "lastname", "email", "password1", "password2"]