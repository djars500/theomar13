from django.shortcuts import render
from .models import Category,Posts
from django.views.generic.base import View

class Main(View):
    def get(self, request):
        categories = Category.objects.order_by('sort_id')

        posts = Posts.objects.all()
        context = {
            "posts" : posts,
            "categories": categories
        }

        return render(request, 'main/main.html',context)

class Article_List(View):
    def get(self,request, url):
        categories = Category.objects.order_by('sort_id')
        category = Category.objects.get(url=url)
        posts = category.posts.all()
        context = {
            "category": category,
            "categories": categories,
            "posts": posts
        }
        return render(request, 'main/article_list.html', context)

class ArticleDetail(View):
    def get(self,request, url):
        categories = Category.objects.order_by('sort_id')
        article = Posts.objects.get(url=url)
        context = {
            "categories": categories,
            "article": article
        }
        return render(request, 'main/single_list.html', context)
