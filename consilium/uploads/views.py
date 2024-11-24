from django.shortcuts import render, redirect
from .models import MediaPost
from .forms import MediaPostForm


def media_list(request):
    posts = MediaPost.objects.order_by('-created_at')  # Order by newest first
    return render(request, 'uploads/media_list.html', {'posts': posts})


def upload_media(request):
    if request.method == 'POST':
        form = MediaPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaPostForm()
    return render(request, 'uploads/upload_media.html', {'form': form})
