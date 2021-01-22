from django.shortcuts import render
from rest_framework import generics
from .models import Category, Recipe, Ingredient, Comment, Like, RecipeView
from .serializers import CategoryListSerializer, RecipeListSerializer, RecipeDetailSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.
class CategoryList(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class RecipeList(generics.ListAPIView):
    serializer_class = RecipeListSerializer
    queryset = Recipe.objects.all()


    