from django.urls import path
from .views import CategoryList, RecipeList, RecipeDetail

urlpatterns = [
    path("", CategoryList.as_view(), name="categoryList"),
    path("<category>/recipeList", RecipeList.as_view(), name="recipeList"),
    path("recipe/<title>/", RecipeDetail.as_view(), name="recipeDetail")
]