from django.db import models
from django.utils import timezone

class CategoryModel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class PostBlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogimages/', null=True, blank=True)

    def __str__(self):
        return self.title


class PostWorkModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogimages/', null=True, blank=True)

    def __str__(self):
        return self.title