from django.shortcuts import render

# Create your views here.
def homepage(request):
    squery = (request.GET) or None

    if not squery or squery['searchquery']=="":
        squery = None

    if squery is None:
        return render(request, 'homepage/main.html', {})
    else:
        from products.models import Products
        obj = Products.objects.filter(name__contains = squery['searchquery'])
        return render(request, 'homepage/searchresults.html', {'res': obj})