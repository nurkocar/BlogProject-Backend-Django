from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = (
        'username',
        'email'
    )
    
