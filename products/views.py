from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def product_home(request):

    return HttpResponse(f'<center><h1>Welcome to Products Home</h1><hr></center>')

def product_specific(request, id = 0):

    objs = Products.objects.all()
    return HttpResponse(f'<center><h1>Product with id {id} is {objs[id-1]}</h1><hr></center>')
