
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from filemanager.models import *
from django.contrib.auth import authenticate
class RegisterAuthenticationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    

class LoginAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True)
    password =forms.CharField(widget=forms.PasswordInput)