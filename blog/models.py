from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name="posts",
    )
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Meta:
    ordering = ["-created_at"]
    verbose_name_plural = "Blog Posts"
    def __str__(self):
        return self.title


