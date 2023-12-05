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
