from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    #url(r'^forum/', include('forum.urls')),  
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
    url(r'^question/add/$', views.QuestionCreate.as_view(), name = "questionAdd"),
    url(r'^answer/(?P<pk>[0-9]+)/$', views.AnswerCreate.as_view(), name = "answerAdd"),
    url(r'^upvote/(?P<pk>[0-9]+)/$', views.upvote, name = "answerUpvote"),

]
