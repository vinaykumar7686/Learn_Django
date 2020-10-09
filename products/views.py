from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def product_home(request):

    # return HttpResponse(f'<center><h1>Welcome to Products Home</h1><hr></center>')    
    obj = Products.objects.all()
    return render(request, 'product_templates/Products_Home.html', context = {'t_count':len(obj),'objects': obj})

def product_specific(request, pk = 1):
    try:
        obj = Products.objects.get(id = pk)
        #return HttpResponse(f'<center><h1>Product with id {id} is {objs[id-1]}</h1><hr></center>')

        context = {
            'Identification No. : ': pk,
            'name': obj.name, 
            'content': obj.content, 
            'price': obj.price,
        }

        return render(request, 'product_templates/product_detail.html', context = context)
        
    except Exception as e:
        print(e)
        return HttpResponse(f'Product with id {pk} not found!!')
