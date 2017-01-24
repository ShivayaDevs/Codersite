from django.conf.urls import url

from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    
    url(r'add/$', views.ArticleCreate.as_view(), name = 'article-add'),

    # url(r'ques/(?P<pk>[0-9]+)/$', views.QuestionUpdate.as_view(), name = 'QuestionUpdate')


]