from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        widgets = {
                "username": forms.TextInput(attrs={'class': 'form-control'}),
                "password1": forms.PasswordInput(attrs={'class': 'form-control'}),
                "password2": forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get('password')

        user = authenticate(username=username,password=password)
        if not user:
            raise forms.ValidationError('Invalid Username or Password')
        else:
            self.user_cache=user
        return self.cleaned_data



