from django.db import models
from django.utils import timezone

class CategoryModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PostModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title