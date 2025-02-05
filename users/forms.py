from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()    
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Insert your name',

    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={

    #         }
    #     )
    # )    