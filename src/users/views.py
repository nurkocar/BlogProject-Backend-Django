from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from blog import serializers
from rest_framework import status
from .models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer, RegisterSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
@api_view(['GET', 'PUT'])
def Profile_get_update(request, id):
    
    if request.method == 'GET':
        serializer = ProfileSerializer(request.user.profile)
        
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ProfileSerializer(request.user.profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            data = {
                'message': 'Profile is updated successfully!'
            }
            
            return Response(data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
