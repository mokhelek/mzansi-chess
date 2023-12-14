from django import forms 

from .models import *
from django_quill.fields import QuillField
from django_quill.forms import QuillFormField

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournaments
        fields = '__all__'
        exclude = ('owner',"slug","featured_tournament",)