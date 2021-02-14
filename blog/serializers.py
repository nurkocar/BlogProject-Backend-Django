from django.db.models import fields
from rest_framework import serializers
from .models import Category, Recipe, Ingredient, Comment

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'recipe_count',
            'img'
        )
    # def get_category(self, obj):
    #     return obj.get_category_display()
        
class IngredientSerializer(serializers.ModelSerializer):
    recipe = serializers.StringRelatedField()
    # author = serializers.StringRelatedField()
    class Meta:
        model = Ingredient
        fields = (
            'id',
            # 'author',
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
    author = serializers.StringRelatedField()
    class Meta:
        model = Recipe
        fields = (
            'id',
            'author',
            'title',
            'image',
            'count_like',
            'count_ingredient',
            'method',
            'published_date',
            'info'           
        )
        
class RecipeDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only = True)
    status = serializers.ChoiceField(choices=Recipe.OPTIONS)
    category = CategoryListSerializer()
    ingredients = IngredientSerializer(many=True)
    comments = CommentSerializer(many = True)
    author = serializers.StringRelatedField()
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
            'status',
            'owner',
            'count_comment',
            'count_recipeview',
            'count_like',
            'count_ingredient',
            'ingredients',
            'comments'           
        )
        
    def get_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False

class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    
    
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = (
            'category',
            'title',
            'method',
            'image',
            'status',
            'ingredients'                      
        )
        
        

        
        

