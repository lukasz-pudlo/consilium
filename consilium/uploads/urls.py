from django.urls import path
from uploads.views import MediaPostFormView
from . import views

urlpatterns = [
    path('', views.media_list, name='media_list'),
    path('upload/', MediaPostFormView.as_view(), name='upload_media'),
]
