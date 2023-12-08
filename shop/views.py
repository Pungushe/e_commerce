from django.http import HttpResponse
from django.shortcuts import render
from . models import Product


def frontpage(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/frontpage.html', context)

def products(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        'product': product
    }
    return render(request, 'shop/products-detail.html', context=context)

def add_product(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        image=request.FILES['upload']

        product = Product(name=name, price=price, description=description, image=image)
        product.save()
    return render(request, 'shop/add-product.html')
