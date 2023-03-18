from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('team/<int:pk>/', team, name='team'),
    path('my_teams', users_fav_teams, name='users_fav_teams'),
]