from  django import forms
from .models import Article
from practice.models import Category

class ArticleForm(forms.ModelForm):

  class Meta:
    model = Article
    fields = ['title', 'content', 'category']
    widgets = {
      'content': forms.Textarea(attrs={ 'rows': 12, 'class':'form-control'}),
      'title' : forms.TextInput(attrs = {'class':'form-control'}),
    }