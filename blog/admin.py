from django.contrib import admin
from blog.models import CategoryModel, PostBlogModel, PostWorkModel

admin.site.register(CategoryModel)
admin.site.register(PostBlogModel)
admin.site.register(PostWorkModel)

