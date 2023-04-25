from django.shortcuts import render, redirect
from .cart import Cart
from fanshop.models import Product


def add_to_cart(request, pk):
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.add_product(product)
    cart.save()
    return redirect('/')


def show_cart(request):
    cart = Cart(request)
    print(cart.__dict__)
    return render(request, 'cart/show_cart.html', {'cart': cart})
