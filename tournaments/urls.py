from django.urls import path
from .import views

app_name = 'tournaments'

urlpatterns = [
    path("",views.tournaments,name='tournaments'),
    path("<slug:slug_tournament>/",views.tournament_details,name='tournament_details'),
    path("add", views.addTournament, name = "addTournament")
]