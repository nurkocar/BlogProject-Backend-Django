from rest_framework import serializers
from .models import Category, Recipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'recipe_count'
        )
        
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'image',
            'count_like',
            'count_ingredients',
            
        )


