from django.contrib.auth import get_user_model
from django import forms
# from django.contrib.auth.models import User

User = get_user_model()
restricted_unames = ['abc']

class RegisterForm(forms.Form):

    

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label = "Password",
        widget = forms.PasswordInput
    )
    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        qs = User.objects.filter(username__iexact = username)

        if qs or len(username)<3  or username in restricted_unames:
            raise forms.ValidationError("Username can't be used. Please try again with different username.")
        
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        qs = User.objects.filter(email__iexact = email)

        if qs:
            raise forms.ValidationError('Email already taken')
        
        return email

    

    




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        qs = User.objects.filter(username__iexact = username)

        if not qs:
            raise forms.ValidationError("User Not Found!!")
        
        return username
    
    