from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_application, name='submit_application'),
    path('', views.application_list, name='application_list'),
    path('<int:pk>/', views.application_detail, name='application_detail'),
]
