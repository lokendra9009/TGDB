from django.http import HttpResponse
from .models import Author, Tag, Category,Post
import datetime
from django import template
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.conf import settings


def index(request):
    return HttpResponse("Hello Django")


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
    posts = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'posts': posts})


def post_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )


def post_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)


