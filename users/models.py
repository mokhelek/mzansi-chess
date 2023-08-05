from django.db import models
from django.contrib.auth.models import User 


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300,blank=True, default=" ")
    avatar = models.ImageField(null=True, upload_to="images" , default="user-icon-image-placeholder.jpg" )  
    email = models.EmailField(default=" ")
    lichessAccount = models.URLField(default=" ")
    chessDotCom = models.URLField(default=" ")


    date_created = models.DateField(auto_now_add=True)
    
 
    def __str__(self):
        return str(self.name.username)
 
