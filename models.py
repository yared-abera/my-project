from django.db import models
 
class Post(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
    def str(self):
        return self.name
    
class Comment(models.Model):
     comment=models.TextField()
     created_at=models.DateTimeField(auto_now_add=True)
     modified_at=models.DateTimeField(auto_now=True)
     post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
