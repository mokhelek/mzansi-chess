from django.contrib import admin
from .models import *
from tournaments.models import *
from blog.models import *
from users.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Ratings)
admin.site.register(RatingsWorld)
admin.site.register(Tournaments)
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    pass
