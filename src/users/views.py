from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from blog import serializers
from rest_framework import status
from .models import Profile
from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer, RegisterSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
# class LoginView(views.APIView):
#     def post(self, request, format=None):
#         data = request.data

#         username = data.get('username', None)
#         password = data.get('password', None)

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)

#                 return Response(status=status.HTTP_200_OK)
#             else:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
    
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
    
# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
