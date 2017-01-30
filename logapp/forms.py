from django.contrib.auth.forms import AuthenticationForm 
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class RegistrationForm(forms.Form):
    error_messages = {
        'duplicate_username': 'Username already exists'
    }
    firstname = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(attrs = {'class' : 'form-control'}))
    lastname = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs = {'class' : 'form-control'}))
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs = {'class' : 'form-control'}))
    email = forms.EmailField(label='Email', max_length=30, widget=forms.TextInput(attrs = {'class' : 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1'}))
    password2 = forms.CharField(label='Password (Again)',widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2'}))

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError( self.error_messages['duplicate_username'],  code='duplicate_username',)
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username

        raise forms.ValidationError(
                ('That username exists in our system. Please try another.')
            )

