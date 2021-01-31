from django.shortcuts import render
from django.views.generic import ListView
from blog.models import PostModel

class TopView(ListView):
    template_name = 'top.html'
    model = PostModel