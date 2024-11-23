from django.db import models
from django.core.validators import FileExtensionValidator


class MediaUpload(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    media_file = models.FileField(
        upload_to='uploads/',
        validators=[FileExtensionValidator(
            ['jpg', 'jpeg', 'png', 'mp4', 'mov'])],
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Unnamed Media"
