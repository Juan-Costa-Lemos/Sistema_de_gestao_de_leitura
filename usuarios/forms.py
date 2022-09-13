from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    GENERO_CHOICES = (
        ("Fantasia","Fantasia"),
        ("Humor","Humor"), 
        ("Literatura Brasileira","Literatura Brasileira"), 
        ("Romance","Romance"), 
        ("Autoajuda","Autoajuda"), 
        ("Biografia","Biografia"), 
        ("Ficção científica","Ficção científica"),
        ("Distopia","Distopia" ),
        ("Ação e aventura","Ação e aventura"),
        ("Horror","Horror"),
        ("Thriller e Suspense","Thriller e Suspense")
    )
    Email = forms.EmailField()
    Genero_Favorito = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username','Email','Genero_Favorito','password1','password2']