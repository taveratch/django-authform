from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User;
from django.core import serializers
# from django.contrib.auth.models import User
import django.contrib.auth as auth
import json
# Create your views here.
# ==== Views ====

def index(request):
    return HttpResponseRedirect(reverse('authform:signin'))

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def success(request):
    print(request.session['user'])
    user = request.session['user']
    return render(request, 'success.html', {'message': "Success : (%s)" % user})

def fail(request):
    return render(request, 'fail.html')

# ==== APIs ====
def signin_api(request):
    username = request.POST['username']
    password = request.POST['password']
    auth_user = authenticate(username, password)
    if(auth_user is not None):
        request.session['user'] = auth_user
        print(request.user)
        return HttpResponseRedirect(reverse('authform:success'))
    else:
        return HttpResponseRedirect(reverse('authform:signin'))

def signup_api(request):
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm-password']
    if (password != confirm_password):
        return HttpResponseRedirect(reverse('authform:signup'))
    if (not isExist(username)):
        user = newUser(username, password)
        request.session['user'] = user
        return HttpResponseRedirect(reverse('authform:success'))
    else:
        return HttpResponse('Username already exist')

def isExist(username):
    for user in User.objects.all():
        if (user.username == username):
            return True
    return False

def newUser(username, password):
    user = User(username=username, password=password)
    user.save()
    return user;

def authenticate(username, password):
    for user in User.objects.all():
        if (user.isEquals(username, password)):
            return user
    return None
