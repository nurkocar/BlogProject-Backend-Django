from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from .models import Category, Recipe, Ingredient, Comment, Like, RecipeView
from .serializers import CategoryListSerializer, RecipeListSerializer, RecipeDetailSerializer, RecipeCreateUpdateSerializer, IngredientSerializer, CommentCreateSerializer
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
    
class CommentCreate(APIView):
    
    serializer_class = CommentCreateSerializer
    
    def postComment(self, request, id):
        recipe = get_object_or_404(Recipe, id = id)
        serializer = CommentCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user, recipe = recipe)
            return Response(serializer.data, status = 200)
        else:
            return Response({'errors': serializer.errors}, status = 400)    
    
class RecipeCreate(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    
# class RecipeUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = 
    
    
    
    
    


    