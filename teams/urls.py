from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('team/<slug:slug>/', team, name='team'),
    path('teams/', Teams.as_view(), name='teams'),
    path('my_teams/', users_fav_teams, name='users_fav_teams'),
]