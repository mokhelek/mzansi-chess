from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User 
from .forms import TournamentForm

from users.models import Profile

# Create your views here.


def tournament_details(request,slug_tournament):
    tournament = Tournaments.objects.get(slug=slug_tournament)
    other_tournaments = Tournaments.objects.exclude(slug=slug_tournament)[0:4:-1]    
    context={
        "tournament":tournament,
        "other_tournaments":other_tournaments}
    return render(request,"tournaments/tournament.html",context)


def tournaments(request):
    tournaments = Tournaments.objects.all()[::-1]
    context = {"tournaments":tournaments}
    return render(request,'tournaments/tournamentsList.html',context)


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
            return redirect("main:home")

    context = { "addTournamentForm": addTournamentForm }
    return render(request,"tournaments/add_tournament.html",context)