from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser as User


class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Email',
        'class': 'form-input',
        'id': 'txt-input',
        'name': 'email',
        'required': 'true'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-input',
        'name': 'password',
        'id': 'pwd',
        'required': 'true'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-input',
        'id': 'txt-input',
        'name': 'username',
        'required': 'true'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'form-input',
        'id': 'txt-input',
        'name': 'email',
        'required': 'true'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-input',
        'name': 'password',
        'id': 'pwd',
        'required': 'true'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'form-input',
        'name': 'password',
        'id': 'pwd',
        'required': 'true'
    }))