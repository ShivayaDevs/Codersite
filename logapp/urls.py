# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
app_name = 'logapp'

urlpatterns = [
    url(r'^$', views.home, name='home'),
]