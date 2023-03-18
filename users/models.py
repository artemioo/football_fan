from django.db import models

from django.contrib.auth.models import User
from teams.models import Team


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    favorite_teams = models.ManyToManyField(Team, null=True, blank=True, related_name='fav_teams')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)
