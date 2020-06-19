from planet.models import *
from django import forms

class CreateCommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ['author_name', 'text', ]