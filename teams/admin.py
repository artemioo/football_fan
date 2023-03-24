from django.contrib import admin
from .models import Team, Match
from django.contrib.auth.models import User, Permission

from django.contrib.contenttypes.models import ContentType



@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    actions = ['make_finished', ]

    @admin.action(description='Сделать матчи завершенными')
    def make_finished(self, request, queryset):
        finished_matches = queryset.update(finished=True)
        if finished_matches == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{finished_matches} были обновлены'
        self.message_user(request, f'{message_bit}')


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