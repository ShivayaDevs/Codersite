"""Codersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views
from logapp.forms import LoginForm
from logapp.views import register_page



urlpatterns = [
    url(r'^forum/', include('forum.urls', namespace = "forum")),  
    url(r'^admin/', admin.site.urls),
    url(r'^practice/', include('practice.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^register/', register_page, name = 'register'),
    url(r'^', include('logapp.urls')),
    url(r'^login/$', views.login, {'template_name': 'logapp/login.html', 'authentication_form' : LoginForm}, name = 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'},name = 'logout'),  
]

if settings.DEBUG :
  urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



