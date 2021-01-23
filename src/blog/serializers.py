from rest_framework import serializers
from .models import Category, Recipe, Ingredient

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'recipe_count'
        )
    def get_recipe_count(self, obj):
        return obj.get_recipe_count_display()
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name'
        ]
        
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
    def get_count_like(self, obj):
        return obj.get_count_like_display()
    
    def get_count_ingredients(self, obj):
        return obj.get_count_ingredients_display()
        
class RecipeDetailSerializer(serializers.ModelSerializer):
    
    ingredient = IngredientSerializer(many=True, read_only=True)
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
            'ingredient'
            'count_ingredients',
            'comments'           
        )

class RecipeCreateSerializer(serializers.ModelSerializer):
    
    ingredient = IngredientSerializer(many=True, read_only = True)
    class Meta:
        model = Recipe
        fields = (
            'title',
            'ingredient',
            'method',
            'image'                  
        )
        
        

