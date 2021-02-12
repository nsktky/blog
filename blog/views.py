from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from blog.models import PostBlogModel, PostWorkModel, CategoryModel


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


class CategoryListView(ListView):
    template_name = 'categorylist.html'
    model = CategoryModel


class CategoryDetailView(ListView):
    template_name = 'categorydetail.html'
    model = PostBlogModel

    def get_queryset(self):
            # urlsから渡されるslugをオブジェクト化
            slug = self.kwargs['slug']
            # CategoryModelのsulgと上記のslugが一致するものを取得
            self.category = get_object_or_404(CategoryModel, slug=slug)
            # PostBlogModel内のcategoryと上記categoryが一致するデータのクエリセットを取得
            qs = super().get_queryset().filter(category=self.category).order_by('-created_at')
            return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = self.category
        return context

class AboutView(TemplateView):
    template_name = 'about.html'