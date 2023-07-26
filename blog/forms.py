from django import forms 

from .models import *
from django_quill.fields import QuillField
from django_quill.forms import QuillFormField

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
        exclude = ('owner',"slug","approved","featured_article",)