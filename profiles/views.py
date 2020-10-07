from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def profiles_home(request):
    return HttpResponse('<center><h1>Welcome to Profiles Home</h1></center>')
