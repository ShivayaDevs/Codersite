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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from logapp.forms import LoginForm
from logapp.views import register_page


urlpatterns = [
    url(r'^articles/', include('articles.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'', include('logapp.urls')),
    url(r'^register/', register_page, name = 'register'),
    url(r'^login/$', views.login, {'template_name': 'logapp/login.html', 'authentication_form' : LoginForm}, name = 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),  
 ]
