from django.urls import path
from .views import CategoryList, RecipeList, RecipeDetail, RecipeCreate

urlpatterns = [
    path("", CategoryList.as_view(), name="categoryList"),
    path("create/", RecipeCreate.as_view(), name="recipeCreate"),
    path("<category>/", RecipeList.as_view(), name="recipeList"),
    path("recipe/<int:id>/", RecipeDetail.as_view(), name="recipeDetail")
    
]

