from django import forms
from .models import tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class tweetform(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['text','photo']

class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        


