
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User 

from .forms import ArticleForm, TournamentForm
from users.models import Profile

# Create your views here.


def read_article(request,slug):
    article = Articles.objects.get(slug = slug)
    articles = Articles.objects.exclude(slug=slug)[0:3:-1]
    context = {"article":article,"articles":articles}
    return render(request,"blog/read_article.html", context)

def ratings(request):
    player_info = Ratings.objects.all().order_by("position")
    player_info_world = RatingsWorld.objects.all().order_by("position")
    context = {
        "player_info":player_info,
        "player_info_world":player_info_world
        }
    return render(request, "blog/ratings.html",context)

def tournaments(request):
    tournaments = Tournaments.objects.all()[::-1]
    context = {"tournaments":tournaments}
    return render(request,'blog/tournamentsList.html',context)

def articlesList(request):
    articles = Articles.objects.all().order_by("-date_posted")

    context = {
        "articles":articles,
    }
    return render(request,"blog/articlesList.html",context)


def tournament_details(request,slug_tournament):
    tournament = Tournaments.objects.get(slug=slug_tournament)
    other_tournaments = Tournaments.objects.exclude(slug=slug_tournament)[0:4:-1]    
    context={
        "tournament":tournament,
        "other_tournaments":other_tournaments}
    return render(request,"blog/tournament.html",context)

def addArticle(request):
    authenticatedUser = Profile.objects.get(name = request.user)
    if request.method != 'POST':
        addArticleForm = ArticleForm()
    else:
        addArticleForm = ArticleForm(request.POST, request.FILES)
        if addArticleForm.is_valid():
            newArticle = addArticleForm.save(commit=False)
            newArticle.owner = authenticatedUser
            # addArticle.save()
            addArticleForm.save()
            return redirect("blog:blog")

    context = { "addArticleForm": addArticleForm }
    return render(request,"blog/add_article.html",context)

def addTournament(request):
    authenticatedUser = Profile.objects.get(name = request.user)
    if request.method != 'POST':
        addTournamentForm = TournamentForm()
    else:
        addTournamentForm = TournamentForm(request.POST, request.FILES)
        if addTournamentForm.is_valid():
            newTournament = addTournamentForm.save(commit=False)
            newTournament.owner = authenticatedUser
            addTournamentForm.save()
            return redirect("blog:blog")

    context = { "addTournamentForm": addTournamentForm }
    return render(request,"blog/add_tournament.html",context)