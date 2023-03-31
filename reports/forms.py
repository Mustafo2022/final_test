from django import forms
from .models import ReportModel


class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        fields = ['title', 'message']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Your Report name',
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Report Message',
                'class': 'form-control',
            })
        }