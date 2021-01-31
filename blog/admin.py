from django.contrib import admin
from blog.models import CategoryModel, PostModel

admin.site.register(CategoryModel)
admin.site.register(PostModel)
