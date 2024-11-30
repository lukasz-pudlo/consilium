from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import MediaPost, MediaFile
from .forms import MediaPostForm
from django.views.generic.edit import FormView


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


class MediaPostFormView(FormView):
    form_class = MediaPostForm
    template_name = "uploads/upload_media.html"
    success_url = reverse_lazy("media_list")

    def form_valid(self, form):
        files = self.request.FILES.getlist('media_files')
        post = MediaPost.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description']
        )
        for file in files:
            media_type = 'image' if file.content_type.startswith(
                'image') else 'video'
            MediaFile.objects.create(
                post=post, media_type=media_type, file=file)
        return super().form_valid(form)
