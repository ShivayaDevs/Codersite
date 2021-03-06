from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Article
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from practice.models import Category
from django.forms import ModelForm, TextInput

# Create your views here.
from .forms import ArticleForm
# Return All Articles
class IndexView(generic.ListView) :
    template_name = "articles/index.html"
    context_object_name = "all_articles"

    def get_queryset(self) :
        return Article.objects.all()

class DetailView(generic.DetailView) :
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleCreate(CreateView) :
    # model = Article
    # What fields needed
    form_class = ArticleForm
    template_name = 'articles/article_form.html'

    # fields = ['title','content','category']
    success_url = reverse_lazy('logapp:home')

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.date_added = datetime.now()
        self.user = self.request.user
        self.object.save()
        return super(ArticleCreate, self).form_valid(form)

