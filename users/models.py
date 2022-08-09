
from django.db import models
from django.contrib.auth.models import User 
#from blogyapp.models import Entry



# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE ,default=1 ) # this has the username inside
    bio = models.CharField(max_length=300,blank=True, default="Hey There I'm using Bloggy")
    avatar = models.ImageField(null=True, upload_to="images" )  #default="default.png"
    about = models.TextField(null=True , blank=True)
    
    date_created = models.DateField(auto_now=True)
    
 
    def __str__(self):
        return str(self.name.username)
 
