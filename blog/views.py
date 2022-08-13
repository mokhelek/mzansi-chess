from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User 

# Create your views here.

def blog(request):
    articles = Articles.objects.all().order_by("-date_posted")
    tournaments = Tournaments.objects.all()[:3:-1]

    paginator = Paginator(articles, 3) 
   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    featured_article = Articles.objects.filter(featured_article=True)
    
    context = {"articles":page_obj,"tournaments":tournaments,"featured_article":featured_article}
    
    return render(request, "blog/articles_list.html", context)

def read_article(request,article_id):
    article = Articles.objects.get(id = article_id)
    articles = Articles.objects.exclude(id=article_id)[0:3:-1]
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

def tournament_details(request,tournament_id):
    tournament = Tournaments.objects.get(id=tournament_id)
    other_tournaments = Tournaments.objects.exclude(id=tournament_id)[0:4:-1]
    
    context={"tournament":tournament,"other_tournaments":other_tournaments}
    return render(request,"blog/tournament.html",context)
