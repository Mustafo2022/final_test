from django import forms
from django.core.exceptions import ValidationError
from .models import UserModel


class AccountForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'form-control'
            }),

            'user_image': forms.FileInput(attrs={
                'placeholder': 'First name',
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            }),

        }


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': 'input100'
    }))

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password', 'bio']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First name',
                'class': 'input100'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last name',
                'class': 'input100'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'input100'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'input100',
                'name': 'email'
            }),

            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'input100'
            }),

            'bio': forms.Textarea(attrs={
                'placeholder': 'Talk us about your self',
                'class': 'input100 bio'
            }),
        }

        def clean_confirm_password(self):
            if self.clened_data['confirm_password'] != self.cleaned_data['password']:
                raise ValidationError('Passwords is not same!')

            return self.cleaned_data['confirm_password']
