from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm( UserCreationForm):
 username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your User Name'}))
 email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email Address'}))
 password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password1'}))
 password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password2'}))
 class Meta:
    model=User
    fields=['username','email','password1','password2']