from django.contrib.auth import get_user_model
from django import forms
# from django.contrib.auth.models import User

User = get_user_model()

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
    
    