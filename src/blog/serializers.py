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
    # def get_recipe_count(self, obj):
    #     return obj.get_recipe_count_display()
        
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
            'content'
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
            'count_ingredients',            
        )
        
class RecipeDetailSerializer(serializers.ModelSerializer):
    
    ingredients = IngredientSerializer(many=True, read_only=True)
    comments = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'count_ingredients',
            'image',
            'author',
            'count_comment',
            'count_recipeview',
            'count_like',
            'ingredients',
            'comments'           
        )

class RecipeCreateSerializer(serializers.ModelSerializer):
    
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = (
            'title',
            'ingredients',
            'method',
            'image'                  
        )
        
        

