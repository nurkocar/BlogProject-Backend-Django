from django.shortcuts import render
from rest_framework import generics
from .models import Category, Recipe, Ingredient, Comment, Like, RecipeView
from .serializers import CategoryListSerializer, RecipeListSerializer, RecipeDetailSerializer, RecipeCreateSerializer, IngredientSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.
class CategoryList(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class RecipeList(generics.ListAPIView):
    
    serializer_class = RecipeListSerializer
    
    def get_queryset(self):
        queryset = Recipe.objects.all()
        category = self.kwargs['category']
        queryset = queryset.filter(category__name = category)
        return queryset
    
class RecipeDetail(generics.RetrieveAPIView):
    serializer_class = RecipeDetailSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        queryset = Recipe.objects.all()
        id = self.kwargs['id']
        queryset = queryset.filter(id = id)
        return queryset
    
class IngredientCreate(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]
    
class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class RecipeCreate(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateSerializer
    permission_classes = [IsAuthenticated]
    
    
    
    


    