from django.urls import path
from .views import RegisterView, Profile_get_update
from rest_framework import views as rest_views
# from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('profile/<int:id>', Profile_get_update, name = 'profile'),
    path('profile/<int:id>/update/', Profile_get_update, name = 'profileUpdate'),
]