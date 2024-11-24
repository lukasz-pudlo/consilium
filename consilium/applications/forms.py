from django import forms
from .models import GrantApplication


class GrantApplicationForm(forms.ModelForm):
    class Meta:
        model = GrantApplication
        exclude = []  # Include all fields
        widgets = {
            'required_date': forms.DateInput(attrs={'type': 'date'}),
            'signed_date': forms.DateInput(attrs={'type': 'date'}),
        }
