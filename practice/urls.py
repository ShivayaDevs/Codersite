from django.conf.urls import url
from . import views

app_name = 'practice'

urlpatterns = [
  url(r'^$',  views.IndexView.as_view(), name='index'),
  url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
  url(r'^submit/(?P<question_id>[0-9]+)/$', views.submit, name='submit')
]