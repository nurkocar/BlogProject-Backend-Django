from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import Category, Recipe, Ingredient, Comment, Like, RecipeView
from .serializers import CategoryListSerializer, RecipeListSerializer, RecipeDetailSerializer, RecipeCreateUpdateSerializer, IngredientSerializer, CommentCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwner
from .pagination import RecipePageNumberPagination
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.
class CategoryList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()
    
class UserRecipeList(generics.ListAPIView):
    serializer_class = RecipeListSerializer
    pagination_class = RecipePageNumberPagination
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        queryset = Recipe.objects.filter(author = self.request.user)
        return queryset

class RecipeList(generics.ListAPIView):
    
    serializer_class = RecipeListSerializer
    permission_classes = [AllowAny]
    pagination_class = RecipePageNumberPagination
    
    
    def get_queryset(self):
        queryset = Recipe.objects.filter(status = 'p')
        category = self.kwargs['category']
        queryset = queryset.filter(category__name = category)
        return queryset
    
class RecipeDetail(generics.RetrieveAPIView):
    serializer_class = RecipeDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    lookup_field = 'id'
    
class IngredientCreate(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]
    
class IngredientUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'id'
    
class CommentCreate(APIView):
    
    serializer_class = CommentCreateSerializer
    
    def post(self, request, id):
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
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
    
class RecipeUpdate(generics.RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'id'
    
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)
        
class RecipeDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    lookup_field = 'id'
    
class LikeCreate(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        obj = get_object_or_404(Recipe, id = id)
        like_query_set = Like.objects.filter(user = request.user, recipe = obj)
        if like_query_set.exists():
            like_query_set[0].delete()
        else:
            Like.objects.create(user = request.user, recipe = obj)
        
        data = {
            'messages': 'like/unlike operations are succesfull'
        }
        
        return Response(data)
    

    
    
    
    


    