from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm
from .models import MyUser as User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation

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

class CustomPasswordSendEmailForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'form-input',
            'id': 'txt-input',
            'name': 'email',
            'required': 'true'
        }),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError(_('Email field is required'))
        return email
    
class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'New password',
            'class': 'form-input',
            'name': 'password',
            'id': 'pwd',
            'required': 'true'
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm new password',
            'class': 'form-input',
            'name': 'password',
            'id': 'pwd',
            'required': 'true'
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("The two password fields didn't match.")
        
        # Additional custom validation if needed

        return new_password2