from django import forms
from django.core.validators import EmailValidator


class LoginForm(forms.Form):
    email = forms.EmailField(validators=[EmailValidator])
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)