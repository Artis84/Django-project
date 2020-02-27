from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label="Pseudo", max_length=10)
    firstname = forms.CharField(label="Prenom", max_length=10, required=False)
    lastname = forms.CharField(label="Nom", max_length=15, required=False)

    class Meta:
        model = User
        fields = ["username", "lastname", "firstname",
                  "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
