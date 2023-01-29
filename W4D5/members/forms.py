from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    # username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=100) 
    last_name = forms.CharField(max_length=100) 
    dob = forms.CharField(max_length=50)
    address = forms.CharField(max_length=200)
    country_of_origin = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'dob', 'address', 'country_of_origin')