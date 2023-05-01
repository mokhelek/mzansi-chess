from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User 

# Create your views here.

def blog(request):
    articles = Articles.objects.all().order_by("-date_posted")[:3]
    tournaments = Tournaments.objects.all()[:3:-1]

    featured_articles = Articles.objects.filter(featured_article=True)[:2:-1]
    featured_tournaments = Tournaments.objects.filter(featured_tournament=True)[:3:-1]

    
    context = {
        "articles":articles,
        "tournaments":tournaments,
        "featured_articles":featured_articles,
        "featured_tournaments":featured_tournaments,
        }
    
    return render(request, "blog/articles_list.html", context)

def read_article(request,slug):
    article = Articles.objects.get(slug = slug)
    articles = Articles.objects.exclude(slug=slug)[0:3:-1]
    context = {"article":article,"articles":articles}
    return render(request,"blog/read_article.html", context)

def ratings(request):
    player_info = Ratings.objects.all().order_by("position")
    player_info_world = RatingsWorld.objects.all().order_by("position")
    context = {"player_info":player_info,"player_info_world":player_info_world}
    return render(request, "blog/ratings.html",context)

def tournaments(request):
    tournaments = Tournaments.objects.all()[::-1]
    context = {"tournaments":tournaments}
    return render(request,'blog/tournaments.html',context)

def tournament_details(request,slug_tournament):
    tournament = Tournaments.objects.get(slug=slug_tournament)
    print(tournament)
    other_tournaments = Tournaments.objects.exclude(slug=slug_tournament)[0:4:-1]
    
    context={"tournament":tournament,"other_tournaments":other_tournaments}
    return render(request,"blog/tournament.html",context)
