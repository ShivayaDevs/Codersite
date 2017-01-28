from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

@login_required(login_url="login/")
def home(request):
    return render(request,"logapp/home.html")


def register_page(request):
    args = {}
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'],first_name = form.cleaned_data['firstname'], last_name = form.cleaned_data['lastname'])
            return HttpResponseRedirect("/login/")
       
        else:
            args['form'] = form
            print form['username'].errors
            return render_to_response('logapp/register.html', args)

    args['form'] = RegistrationForm()
    print args
    return render_to_response('logapp/register.html',args)