from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    city = forms.CharField(max_length=30, required=True, help_text='Enter you city name.')
    pin_code = forms.IntegerField(required=True, help_text='Required.')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Required. Enter a password.')

    class Meta:
        model = User
        fields = ('first_name',  'email', 'city', 'pin_code','password')

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    username = forms.CharField(max_length=50, required=True, help_text='Required.')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Required. Enter a password.')
    
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password')