from  django import forms
from .models import Article
from practice.models import Category

class ArticleForm(forms.ModelForm):

  category = forms.ModelChoiceField(queryset = Category.objects.all(), widget = forms.Select(attrs={'class': 'form-control', 'name': 'category', 'cols':5}))
  class Meta:
    model = Article
    fields = ['title', 'content', 'category']
    widgets = {
      'content': forms.Textarea(attrs={ 'rows': 12, 'class':'form-control'}),
      'title' : forms.TextInput(attrs = {'class':'form-control'}),
    }

    def __init__(self, u, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()