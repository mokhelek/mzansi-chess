from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    path("",views.blog,name='blog'),
    path("read_article/<int:article_id>/",views.read_article,name='read_article'),
    path("ratings/",views.ratings,name='ratings'),
    
    
    path("tournaments/",views.tournaments,name='tournaments'),
    path("tournament/<int:tournament_id>/",views.tournament_details,name='tournament_details'),
     
]