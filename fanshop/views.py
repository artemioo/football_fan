from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def fanshop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'fanshop/all_products.html', context)
