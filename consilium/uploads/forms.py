from django import forms
from .models import MediaPost


class MediaPostForm(forms.ModelForm):
    class Meta:
        model = MediaPost
        fields = ['title', 'description', 'media_type', 'image', 'video']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        media_type = cleaned_data.get('media_type')
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')

        if media_type == 'image' and not image:
            raise forms.ValidationError(
                "Please upload an image for this post.")
        if media_type == 'video' and not video:
            raise forms.ValidationError("Please upload a video for this post.")
        return cleaned_data
