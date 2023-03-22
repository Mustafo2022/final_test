from django import forms
from .models import Messages


class ContactForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-control',
                'id': 'name',
                'name': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email',
                'class': 'form-control',
                'id': 'name',
                'name': 'email'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'subject',
                'class': 'form-control',
                'id': 'subject',
                'name': 'subject'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
                'class': 'form-control',
                'id': 'message',
                'name': 'message',
                'rows': '5'
            }),
        }