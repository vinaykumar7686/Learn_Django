from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def product_home(request):
    return HttpResponse('<center><h1>Welcome to Products Home</h1></center>')

