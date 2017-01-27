from django.conf.urls import include, url
from django.contrib   import admin
from . import views

app_name = 'practice'

urlpatterns = [
  url(r'^$',  views.IndexView.as_view(), name='index'),
  url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
  url(r'^result/(?P<pk>[0-9]+)/$', views.ResultView.as_view(), name='result'),
  url(r'^submit/(?P<question_id>[0-9]+)/$', views.submit, name='submit')
]