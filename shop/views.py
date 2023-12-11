from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView


class ProductListView(ListView):
    model = Product
    template_name = 'shop/frontpage.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/products-detail.html'
    context_object_name = 'product'
@login_required
def add_product(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        image=request.FILES['upload']
        seller=request.user

        product = Product(name=name, price=price, description=description, image=image, seller=seller)
        product.save()
        return redirect('shop:frontpage')
    return render(request, 'shop/add-product.html')

def update_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.name=request.POST.get('name')
        product.price=request.POST.get('price')
        product.description=request.POST.get('description')
        product.image=request.FILES.get('upload', product.image)
        product.save()
        return redirect('shop:frontpage')

    context = {
        'product': product
    }
    return render(request, 'shop/update-product.html', context)

def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('shop:frontpage')

    context = {
        'product': product
    }
    return render(request, 'shop/delete-product.html', context)

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shop:frontpage')