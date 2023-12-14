
from django.db import models
from django.contrib.auth.models import User

from io import BytesIO
from PIL import Image
from django.core.files import File

from django_quill.fields import QuillField
from django.urls import reverse

from django.utils.text import slugify

from users.models import Profile


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=50)
    new_image = File(im_io, name=image.name)
    return new_image



class Articles(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    title = models.CharField(max_length=200)
    subtitle = models.TextField(max_length=500, null=True, blank=True)
    body = QuillField()
    slug = models.SlugField(max_length=300,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    featured_article = models.BooleanField(null=True, blank=True, default=False)
    approved = models.BooleanField(null=True, blank=True, default=False)

    class Meta:
        verbose_name_plural = "articles"

    def save(self, *args, **kwargs):
        new_image = compress(self.thumbnail)
        self.thumbnail = new_image
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug":self.title})
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f' "{self.title}" by {self.owner}'
