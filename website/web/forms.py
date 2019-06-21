from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username')
    password = forms.CharField(min_length=6, max_length=50, label='Password', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This User is already existing')
        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This Email is already existing')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username')
    password = forms.CharField(min_length=6, max_length=50, label='Password', widget=forms.PasswordInput)



