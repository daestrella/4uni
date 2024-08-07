from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Thread, Reply

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'university', 'signature']

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'body', 'img']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body', 'img']
