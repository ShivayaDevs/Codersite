from django.conf.urls import url

from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'add/$', views.ArticleCreate.as_view(), name = 'article-add'),
]