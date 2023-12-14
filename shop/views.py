from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseNotFound, JsonResponse
import stripe

from . models import OrderDetail, Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def frontpage(request):
    page_obj = products = Product.objects.order_by('id')

    product_name = request.GET.get('search')

    if product_name != '' and product_name is not None:
        page_obj = products.filter(name__icontains=product_name)

    paginator = Paginator(page_obj, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    ordering = ('id')
    context = {
        'page_obj': page_obj,
        'ordering': ordering,
    }
    return render(request, 'shop/frontpage.html', context)


# class ProductListView(ListView):
#     model = Product
#     template_name = 'shop/frontpage.html'
#     context_object_name = 'products'
#     paginate_by = 2
#     ordering = ['id']

class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/detail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context["stripe_publishable_key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context


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

def update_product(request, id):
    product = Product.objects.get(id=id)
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

@csrf_exempt
def create_checkout_session(request, id):
    product = get_object_or_404(Product, pk=id)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": product.name,
                    },
                    "unit_amount": int(product.price * 100),
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("shop:success"))
        + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse("shop:cancel")),
    )
    order = OrderDetail()
    order.product = product
    order.stripe_payment_intent = checkout_session["payment_intent"]
    order.amount = int(product.price * 100)
    order.save()
    return JsonResponse({"sessionId": checkout_session.id})


class PaymentSuccessView(TemplateView):
    template_name = "shop/payment-success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get("session_id")
        if session_id is None:
            return HttpResponseNotFound("shop:frontpage")

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(
            OrderDetail, stripe_payment_intent=session.payment_intent
        )
        order.has_paid = True
        order.save()
        return redirect(request, self.template_name)


class PaymentCancelView(TemplateView):
    template_name = "shop/payment-cancel.html"