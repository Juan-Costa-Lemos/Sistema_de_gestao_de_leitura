from dataclasses import field
import email
from pyexpat import model
from socket import fromshare
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    generoFav = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username','email','generoFav','password1','password2']