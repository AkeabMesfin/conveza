from django import forms
from django.contrib.auth.hashers import make_password
from .models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'password']

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password using set_password, which also handles validation requirements
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
        return user

