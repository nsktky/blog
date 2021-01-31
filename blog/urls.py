from django.contrib import admin
from django.urls import path
from blog.views import TopView

urlpatterns = [
    path('', TopView.as_view(), name='top'),
]
