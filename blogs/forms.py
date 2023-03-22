from django import forms
from .models import Blogs


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'image', 'category', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-control',
                'id': 'name',
                'name': 'name'
            }),
            'image': forms.FileInput(attrs={
                'placeholder': 'Your email',
                'class': 'form-control image_upload',
                'id': 'inputGroupFile02',
                'title': 'Choose File',
                'name': 'email'
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Category (Categories)',
                'class': 'form-control',
                'id': 'subject',
                'name': 'subject'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description',
                'class': 'form-control',
                'id': 'message',
                'name': 'message',
                'rows': '5'
            }),
        }