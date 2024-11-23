from django import forms
from .models import MediaUpload


class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaUpload
        fields = ['title', 'description', 'media_file']
