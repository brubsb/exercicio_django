from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class FormParaCriarUsuario(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email']