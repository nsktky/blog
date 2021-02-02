from django.contrib import admin
from django.urls import path
from blog.views import TopView, WorkView, BlogView, WorkDetailView, BlogDetailView

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('bloglist/', BlogView.as_view(), name='bloglist'),
    path('worklist/', WorkView.as_view(), name='worklist'),
    path('work/<int:pk>/', WorkDetailView.as_view(), name='workdetail'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blogdetail'),
    

]
