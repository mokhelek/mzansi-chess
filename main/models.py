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

# Create your models here.
titles = (
    (" ", " "),
    ("CM", "CM"),
    ("FM", "FM"),
    ("IM", "IM"),
    ("GM", "GM"),
)


class Ratings(models.Model):
    position = models.IntegerField(default=0)
    player_name = models.CharField(max_length=200)
    player_title = models.CharField(max_length=10, choices=titles, default=" ")
    player_rating = models.IntegerField(default=0)
    age = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = "ratings"

    def __str__(self):
        return f"{self.player_title}  {self.player_name}"


class RatingsWorld(models.Model):
    position = models.IntegerField(default=0)
    player_name = models.CharField(max_length=200)
    player_title = models.CharField(max_length=10, choices=titles, default=" ")
    player_rating = models.IntegerField(default=0)
    age = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = "world_ratings"

    def __str__(self):
        return f"{self.player_title}  {self.player_name}"
