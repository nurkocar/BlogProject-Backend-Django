from django.urls import path
from .views import CategoryList, RecipeList, RecipeDetail, RecipeCreate, IngredientCreate, CommentCreate

urlpatterns = [
    path("categoryList/", CategoryList.as_view(), name="categoryList"),
    path("recipeCreate/", RecipeCreate.as_view(), name="recipeCreate"),
    path("ingredientCreate/", IngredientCreate.as_view(), name="ingredientCreate"),
    path("commentCreate/", CommentCreate.as_view(), name="commentCreate"),
    # path("likeCreate/", LikeCreate.as_view(), name="likeCreate"),
    path("<category>/", RecipeList.as_view(), name="recipeList"),
    path("recipeDetail/<int:id>/", RecipeDetail.as_view(), name="recipeDetail")
    
]

