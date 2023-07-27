from django.urls import path
from .import views

app_name = 'blog'


urlpatterns = [
    path("",views.blog,name='blog'),
    path("articles/", views.articlesList , name = "articlesList"),
    path("read_article/<slug:slug>/",views.read_article,name='read_article'),
    path("ratings/",views.ratings,name='ratings'),
    
    
    path("tournaments/",views.tournaments,name='tournaments'),
    path("tournament/<slug:slug_tournament>/",views.tournament_details,name='tournament_details'),

    path("add-article", views.addArticle, name = "addArticle"),
    path("add-tournament", views.addTournament, name = "addTournament")
     
]