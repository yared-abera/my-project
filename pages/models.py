from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
    def str(self):
        return self.name


class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return f"Comment by {self.name} on {self.post.name}"



