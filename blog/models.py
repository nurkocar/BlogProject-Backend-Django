from django.db import models
from django.contrib.auth.models import User



# Create your models here.
def user_directory_path(instance, filename):
    return 'blog/{}/{}'.format(instance.author.id, filename)

class Update(models.Model):
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Category(Update):
    name = models.CharField(max_length=100)
    img = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    @property
    def recipe_count(self):
        return self.recipe_set.count()
    

class Recipe(Update):
    
    OPTIONS = (
        ('d','Draft'),
        ('p','Published')        
    )
    
    category = models.ForeignKey(Category, on_delete = models.PROTECT, default=1)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    info = models.TextField()
    method = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = user_directory_path, default = 'shef.png')
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.title + ' in ' + self.category.name
    
    @property
    def count_comment(self):
        return self.comment_set.all().count()

    @property
    def count_recipeview(self):
        return self.recipeview_set.all().count()
    
    @property
    def count_like(self):
        return self.like_set.all().count()
    
    @property
    def count_ingredient(self):
        return self.ingredient_set.count()
    
    @property
    def ingredients(self):
        return self.ingredient_set.all()
    
    @property
    def comments(self):
        return self.comment_set.all()
    

class Ingredient(Update):
    name = models.CharField(max_length = 50)
    # author = models.ForeignKey(User, on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name + ' is in ' + self.recipe.title
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return (self.user.username + ' comments on ' + self.recipe.title)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    like_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.user.username + ' likes ' + self.recipe.title)
    
class RecipeView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.user.username + ' views ' + self.recipe.title)
    
