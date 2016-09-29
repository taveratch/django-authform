from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User;
# Create your views here.
# ==== Views ====

def index(request):
    return HttpResponseRedirect(reverse('authform:signin'))

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def success(request):
    return render(request, 'success.html')

def fail(request):
    return render(request, 'fail.html')

# ==== APIs ====
def signin_api(request):
    username = request.POST['username']
    password = request.POST['password']
    if(authenticate(username, password)):
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
        newUser(username, password)
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
            return True
    return False
