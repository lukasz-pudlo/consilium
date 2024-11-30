from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class MediaPostForm(forms.Form):
    title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 4}), required=True)
    media_files = MultipleFileField()
