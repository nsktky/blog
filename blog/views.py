from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import PostBlogModel, PostWorkModel


class TopView(ListView):
    template_name = 'top.html'
    context_object_name = 'blog_list'
    queryset = PostBlogModel.objects.order_by('-created_at')[:3]
    model = PostBlogModel

# 2つ目のmodelを扱うため、et_context_data関数を継承して上書きする。
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['work_list'] = PostWorkModel.objects.order_by('-created_at')[:3]
        return context


class WorkView(ListView):
    template_name = 'worklist.html'
    queryset = PostWorkModel.objects.order_by('-created_at')


class BlogView(ListView):
    template_name = 'bloglist.html'
    queryset = PostBlogModel.objects.order_by('-created_at')


class WorkDetailView(DetailView):
    template_name = 'workdetail.html'
    model = PostWorkModel


class BlogDetailView(DetailView):
    template_name = 'blogdetail.html'
    model = PostBlogModel