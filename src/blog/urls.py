from django.urls import path
from .views import CategoryList, UserRecipeList, RecipeList, RecipeDetail, RecipeCreate, RecipeUpdate, RecipeDelete, IngredientCreate, IngredientUpdateDelete, CommentCreate

urlpatterns = [
    path("categoryList/", CategoryList.as_view(), name="categoryList"),
    path("myRecipes/", UserRecipeList.as_view(), name="myRecipesList"),
    path("list/<category>/", RecipeList.as_view(), name="recipeList"),
    path("recipeCreate/", RecipeCreate.as_view(), name="recipeCreate"),
    path("recipeDetail/<int:id>/", RecipeDetail.as_view(), name="recipeDetail"),
    path("recipeUpdate/<int:id>/", RecipeUpdate.as_view(), name="recipeUpdate"),
    path("recipeDelete/<int:id>/", RecipeDelete.as_view(), name="recipeDelete"),
    path("ingredientCreate/", IngredientCreate.as_view(), name="ingredientCreate"),
    path("ingredientUpdate/<int:id>", IngredientUpdateDelete.as_view(), name="ingredientUpdateDelete"),
    path("commentCreate/", CommentCreate.as_view(), name="commentCreate"),
    # path("likeCreate/", LikeCreate.as_view(), name="likeCreate"),   
  
    
]

