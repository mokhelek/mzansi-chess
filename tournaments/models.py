from django.db import models
from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.core.files import File
from django_quill.fields import QuillField
from django.urls import reverse
from django.utils.text import slugify
from users.models import Profile

# Create your models here.


ratingType = (
    (" ", " "),
    ("FIDE Rated", "FIDE Rated"),
    ("Chess SA Rated", "Chess SA Rated"),
    ("Online Rated", "Online Rated"),
    ("Not Rated", "Not Rated"),
)
timeControl = (
    (" ", " "),
    ("Bullet", "Bullet"),
    ("Blitz", "Blitz"),
    ("Rapid", "Rapid"),
    ("Classical", "Classical"),
)


class Tournaments(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    thumbnail_t = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    description = QuillField() # * Go as much in detail as possble
    slug = models.SlugField(blank=True, max_length=300)
    location = models.CharField(max_length=500, null=True, blank=True) # todo : Will later use google API here
    starts = models.DateField(null=True, blank=True)
    ends = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    ratingType = models.CharField(max_length=100, choices=ratingType, default=" ")
    timeControl = models.CharField(max_length=100, choices=timeControl, default=" ")
    date_posted = models.DateField(auto_now_add=True)
    featured_tournament = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        verbose_name_plural = "tournaments"

    def save(self,*args,**kwargs):
        # if not self.slug:
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    # def get_absolute_url(self):
    #     return reverse("tournament_details", kwargs={"slug":self.slug})

    def __str__(self):
        return self.name
