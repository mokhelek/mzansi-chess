
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User 

from .forms import ArticleForm
from users.models import Profile

# Create your views here.


def read_article(request,slug):
    article = Articles.objects.get(slug = slug)
    articles = Articles.objects.exclude(slug=slug)[0:3:-1]
    context = {"article":article,"articles":articles}
    return render(request,"blog/read_article.html", context)


def articlesList(request):
    articles = Articles.objects.all().order_by("-date_posted")

    context = {
        "articles":articles,
    }
    return render(request,"blog/articlesList.html",context)


def addArticle(request):
    authenticatedUser = Profile.objects.get(name = request.user)
    if request.method != 'POST':
        addArticleForm = ArticleForm()
    else:
        addArticleForm = ArticleForm(request.POST, request.FILES)
        if addArticleForm.is_valid():
            newArticle = addArticleForm.save(commit=False)
            newArticle.owner = authenticatedUser
            addArticleForm.save()
            return redirect("blog:blog")

    context = { "addArticleForm": addArticleForm }
    return render(request,"blog/add_article.html",context)
