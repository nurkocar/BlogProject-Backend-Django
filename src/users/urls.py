from django.urls import path
from .views import RegisterView, Profile_get_update
from rest_framework import views as rest_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('profile/<id>', Profile_get_update, name = 'profile'),
    path('profile/update/', Profile_get_update, name = 'profileUpdate')
]