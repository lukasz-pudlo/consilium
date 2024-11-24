from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_list, name='media_list'),
    path('upload/', views.upload_media, name='upload_media'),
]
