from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()

    password = forms.CharField()
    # username = forms.CharField(
    #     label='Name',
    #     widget=forms.TextInput(attrs={
    #         "autofocus": True,
    #         "class": "form-control",
    #         "placeholder": "Enter your username"
    #     })
    # )

    # password = forms.CharField(
    #     label='Pasword',
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password",
    #         "class": "form-control",
    #         "placeholder": "Enter your password"
    #     })
    # )

    class Meta:
        model = User
        fields: list[str] = ['username', 'password']
