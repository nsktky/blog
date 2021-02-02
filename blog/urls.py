from django.contrib import admin
from django.urls import path
from blog.views import TopView, WorkView, BlogView

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('bloglist/', BlogView.as_view(), name='bloglist'),
    path('worklist/', WorkView.as_view(), name='worklist'),

]
