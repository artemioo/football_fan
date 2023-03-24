from django.contrib import admin
from .models import Team, Match
from django.contrib.auth.models import User, Permission

from django.contrib.contenttypes.models import ContentType

admin.site.register(Match)


class MatchesInline(admin.StackedInline):
    model = Match
    fk_name = 'team_home'
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_filter = ('country', )
    search_fields = ('name', 'country')
    prepopulated_fields = {"slug": ("name",)}
    inlines = [MatchesInline, ]
    save_as = True