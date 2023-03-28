from django.urls import path
from .views import *

urlpatterns = [
    path('fanshop/',  fanshop, name='fanshop')    
]