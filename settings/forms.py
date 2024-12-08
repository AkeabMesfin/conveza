from django import forms
from authen.models import User

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'profile_picture']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'id': 'fullName',
                'required': True,
                'placeholder': 'Enter your full name'
            }),
            'username': forms.TextInput(attrs={
                'id': 'username',
                'required': True,
                'placeholder': 'Choose a unique username'
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'placeholder': 'Enter your email'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'id': 'profilePicInput',
                'accept': 'image/*'
            }),
        }
