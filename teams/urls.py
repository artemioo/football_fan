from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home_page'),
    path('update-team/<slug:slug>/', team_update, name='team_update'),
    path('team/<slug:slug>/', TeamDetailView.as_view(), name='team'),
    path('teams/', Teams.as_view(), name='teams'),
    path('my_teams/', users_fav_teams, name='users_fav_teams'),
]