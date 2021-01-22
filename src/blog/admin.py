from django.contrib import admin
import nested_admin
from .models import Category, Recipe, Ingredient, Comment, Like, RecipeView

# Register your models here.

class IngredientsInline(nested_admin.NestedTabularInline):
    model = Ingredient
    extra = 10
    max_num = 30

class RecipeAdmin(nested_admin.NestedModelAdmin):
    model = Recipe
    inlines = [IngredientsInline]
    
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(RecipeView)

