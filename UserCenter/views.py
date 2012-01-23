from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from SoftwareStories.SoftwareProjects.models import Project
from SoftwareStories.UserCenter.forms import UserRegisterationForm

def landing(request):
    logout(request)
    if request.method == 'POST':
        loginForm = AuthenticationForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user and user.is_active:
            login(request,user)
            #fix me
            return HttpResponseRedirect("/project/list/")
        registerForm = UserRegisterationForm()
        #if(loginForm)
    else:
        loginForm = AuthenticationForm()
        registerForm = UserRegisterationForm()
    return render_to_response('landing.html',RequestContext(request,locals()))
    
def accounts_create(request):
    if request.method == 'POST':
        registerForm = UserRegisterationForm(request.POST)
        if registerForm.is_valid():
            newuser = registerForm.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request,user)
            return HttpResponseRedirect("/project/list/")
    else:
        registerForm = UserRegisterationForm()
    return render_to_response('register.html',RequestContext(request,locals()))
