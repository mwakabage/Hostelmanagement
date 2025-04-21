from .models import User,Profile
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'password')  # Add 'role' here

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your middle name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'role': forms.Select(attrs={  # Ensure 'role' is also in `fields`
                'class': 'form-select'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
        }
class ProfileForm(UserChangeForm): 
    password=None
    class Meta:
        model = User
        fields = ("first_name","middle_name","last_name",'profile_image','bio',)