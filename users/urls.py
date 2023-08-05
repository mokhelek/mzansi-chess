from django.urls import path , include
from .import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),  #the login and logout are in here
    
    path('register/', views.register, name='register'),
    path('logout/', views.logout_page, name='logoutpage'),
     
]