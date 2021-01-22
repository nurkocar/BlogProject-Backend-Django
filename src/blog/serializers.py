from rest_framework import serializers
from .models import Category, Recipe, Ingredient

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'recipe_count'
        )
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name'
        ]
        
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
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


