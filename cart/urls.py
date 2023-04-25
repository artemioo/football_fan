from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', show_cart, name='cart'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
]