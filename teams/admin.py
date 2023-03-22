from django.contrib import admin
from .models import Team, Match
from django.contrib.auth.models import User, Permission

from django.contrib.contenttypes.models import ContentType

admin.site.register(Team)
admin.site.register(Match)


