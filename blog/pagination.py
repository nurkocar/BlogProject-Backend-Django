from rest_framework.pagination import PageNumberPagination

class RecipePageNumberPagination(PageNumberPagination):
    page_size = 8
    
    