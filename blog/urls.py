from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path("", views.articlesList , name = "articlesList"),
    path("read/<slug:slug>/",views.read_article,name='read_article'),
    path("add/", views.addArticle, name = "addArticle"),
]