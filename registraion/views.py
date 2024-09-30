from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from app1.models import user
from django.contrib.auth import authenticate


def HomePage(request):
    return render(request,'index.html')

def SignUp(request):
    return render(request,"signup.html")
def Home(request):
    return render(request,'Home.html')
