from django.shortcuts import render
from .models import *
from blog.models import *
from tournaments.models import *
from django.contrib.auth.models import User 

from users.models import Profile

# Create your views here.

def home(request):
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
    
    return render(request, "main/index.html", context)

def ratings(request):
    player_info = Ratings.objects.all().order_by("position")
    player_info_world = RatingsWorld.objects.all().order_by("position")
    context = {
        "player_info":player_info,
        "player_info_world":player_info_world
        }
    return render(request, "main/ratings.html",context)
