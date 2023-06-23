from django import forms 

from .models import *


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = '__all__'
        exclude = ('owner',"slug","approved","featured_article",)