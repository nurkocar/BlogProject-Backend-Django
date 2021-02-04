from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.URLField(
        max_length = 5000, 
        default = 'https://static1.squarespace.com/static/54b7b93ce4b0a3e130d5d232/54e20ebce4b014cdbc3fd71b/5a992947e2c48320418ae5e0/1519987239570/icon.png?format=1500w'
    )
    bio = models.TextField(max_length=500, blank = True)
    
    def __str__(self):
        return f'{self.user.username} Profile'