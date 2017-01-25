from django.conf.urls import include, url
from django.contrib   import admin
from . import views

app_name = 'practice'

urlpatterns = [
  url(r'^$',  views.IndexView.as_view(), name='index'),
  url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^result/(?P<pk>[0-9]+)/$', views.ResultView.as_view(), name='result'),
]