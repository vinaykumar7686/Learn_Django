from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def product_home(request):

    # return HttpResponse(f'<center><h1>Welcome to Products Home</h1><hr></center>')    
    return render(request, 'product_templates/all_products.html', context = None)

def product_specific(request, pk = 0):
    try:
        objs = Products.objects.all()
        #return HttpResponse(f'<center><h1>Product with id {id} is {objs[id-1]}</h1><hr></center>')

        context = {
            'Identification No. : ': pk,
            'name': objs[pk].name, 
            'content': objs[pk].content, 
            'price': objs[pk].price,
        }

        return render(request, 'product_templates/product_detail.html', context = context)
        
    except Exception as e:
        print(e)
        return HttpResponse(f'Product with id {pk} not found!!')
