from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag


def post_lists(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", context={"posts": posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, "blog/post_detail.html", context={"post": post})


def tag_lists(request):
    tags = Tag.objects.all()
    return render(request, "blog/tag_list.html", context={"tags": tags})
