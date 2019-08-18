from django.contrib.auth import authenticate, login, logout
from djngo.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message":None})
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)
