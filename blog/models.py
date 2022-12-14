from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User 

from io import BytesIO
from PIL import Image
from django.core.files import File

from django_quill.fields import QuillField

# Image compression method
def compress(image):
    im =Image.open(image)
    im_io = BytesIO()
    im.save(im_io,'JPEG',quality=50)
    new_image = File(im_io,name=image.name)
    return new_image

# Create your models here.
titles = ( 
          (" "," "),
          ("CM","CM"),
          ("FM","FM"),
          ("IM","IM"),
          ("GM","GM"),
          
          )

class Articles(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400)
    #body = models.TextField()
    body = QuillField()
    date_posted = models.DateTimeField(auto_now=True)
    featured_article = models.BooleanField(null=True,blank=True,default=False)
    class Meta:
        verbose_name_plural = "articles"
        
    def save(self,*args,**kwargs):
        new_image = compress(self.thumbnail)
        self.thumbnail = new_image
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f' "{self.title}" by {self.owner}'
    
class Ratings(models.Model):
    position = models.IntegerField(default=0)
    player_name = models.CharField(max_length=200)
    player_title = models.CharField(max_length=10, choices=titles,default=" ")
    player_rating = models.IntegerField(default=0)
    age = models.CharField(max_length=4)
    
    class Meta:
        verbose_name_plural = "ratings"
    
    def __str__(self): 
        return f"{self.player_title}  {self.player_name}"

class RatingsWorld(models.Model):
    position = models.IntegerField(default=0)
    player_name = models.CharField(max_length=200)
    player_title = models.CharField(max_length=10, choices=titles,default=" ")
    player_rating = models.IntegerField(default=0)
    age = models.CharField(max_length=4)
    
    class Meta:
        verbose_name_plural = "world_ratings"
    
    def __str__(self): 
        return f"{self.player_title}  {self.player_name}"
    
    
class Tournaments(models.Model):
    thumbnail_t = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=200)
    description = QuillField()
    
    starts = models.CharField(max_length=100)
    ends = models.CharField(max_length=100)
    
    date_posted = models.DateField(auto_now=True)
    featured_tournament = models.BooleanField(null=True,blank=True,default=False)

    
    class Meta:
        verbose_name_plural = "tournaments"
    def __str__(self):
        return self.name

