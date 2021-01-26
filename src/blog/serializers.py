from django.db.models import fields
from rest_framework import serializers
from .models import Category, Recipe, Ingredient, Comment

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'recipe_count'
        )
    # def get_category(self, obj):
    #     return obj.get_category_display()
        
class IngredientSerializer(serializers.ModelSerializer):
    recipe = serializers.StringRelatedField()
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'recipe',
            'time_stamp'
        )
        
class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    recipe = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'recipe',
            'comment_time',
            'content',
        )
        
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'content',
        )
        
        
class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'slug',
            'title',
            'image',
            'count_like',
            'count_ingredient',            
        )
        
class RecipeDetailSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    ingredients = IngredientSerializer(many=True)
    comments = CommentSerializer(many = True)
    class Meta:
        model = Recipe
        fields = (
            'id',
            'category',
            'author',
            'title',
            'method',
            'published_date',
            'image',
            'count_comment',
            'count_recipeview',
            'count_like',
            'count_ingredient',
            'ingredients',
            'comments'           
        )

class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = (
            'id',
            'category',
            'title',
            'method',
            'image',
            'status',
            'ingredients'                      
        )
        
        

