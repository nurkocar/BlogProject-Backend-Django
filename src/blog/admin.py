from django.contrib import admin
from .models import Category, Recipe, Ingredient, Comment, Like, RecipeView

# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(RecipeView)

