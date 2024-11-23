from django.shortcuts import render, redirect
from .forms import MediaUploadForm
from .models import MediaUpload


def upload_media(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaUploadForm()
    return render(request, 'upload_media.html', {'form': form})


def media_list(request):
    media = MediaUpload.objects.all()
    return render(request, 'media_list.html', {'media': media})
