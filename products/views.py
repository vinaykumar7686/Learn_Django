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

'''
# Using basic HTML Forms
def create_products(request):
    print(request.GET, request.POST)
    info = request.POST or None

    if info!=None:
        from .forms import create_product_form
        myform = create_product_form(request.POST)
        print(myform.is_valid())
        if myform.is_valid():
            # print(myform.cleaned_data)
            cdata = myform.cleaned_data
            from products.models import Products
            Products.objects.create(name = cdata.get('name'), content = cdata.get('content'), price = cdata.get('price'))
    return render(request, 'product_templates/create_products.html' , {})
    '''

def create_products(request):
    if not request.user.is_staff:
        return HttpResponse("Action Not Allowed")

    # request.user
    from .forms import create_product_form
    myform = create_product_form(request.POST or None)

    if myform.is_valid():
        
        form = myform.save(commit = False)

        # Some Stuff
        form.user = request.user

        form.save()
        
        # redirect to success age or clear the form by "myform = create_product_form()"
        myform = create_product_form()

    return render(request, 'product_templates/create_products.html', {'form': myform})

    
