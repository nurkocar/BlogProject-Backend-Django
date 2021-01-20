from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
class Post(models.Model):
    
    OPTIONS = (
        ('d','Draft'),
        ('p','Published')        
    )
    
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    
    def __str__(self):
        return self.title
    
    def count_comment(self):
        return self.comment_set.all().count()
    
    def count_postview(self):
        return self.postview_set.all().count()
    
    def count_like(self):
        return self.like_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
