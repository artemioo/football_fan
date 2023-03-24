from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from teams.models import Team, Match
from users.models import Profile
from .forms import TeamUpdateForm

from django.contrib import admin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.models import User, Permission
def main(request):
    matches = Match.objects.all()
    context = {'matches': matches}
    return render(request, 'main.html', context)

def users_fav_teams(request):
    profile = request.user.profile
    teams = profile.favorite_teams.all()
    context = {'profile': profile, 'teams': teams}
    return render(request, 'teams/users_fav_teams.html', context)


class Teams(ListView):
    model = Team
    template_name = 'teams/teams_all.html'
    paginate_by = 3

    def get_queryset(self):
        name = self.request.GET.get('team_name', None)
        if name:
            teams = self.model.objects.filter(name__icontains=name)
        else:
            teams = self.model.objects.all()
        return teams

    def get_context_data(self, *args, **kwargs):
        context = super(Teams, self).get_context_data(**kwargs)
        context['team_name'] = self.request.GET.get('team_name', None)
        return context


class TeamDetailView(PermissionRequiredMixin, DetailView):
    # permission_required = 'teams.view_team'
    model = Team
    template_name = 'teams/team.html'

    def get_context_data(self,  *args, **kwargs):
        context = super().get_context_data(**kwargs)
        team = context['team']
        try:
            matches = Match.objects.filter(Q(team_home=team) | Q(team_away=team))
        except:
            matches = None
        context['matches'] = matches
        return context



@permission_required("teams.update_team")
def team_update(request, slug):
    team = Team.objects.get(slug=slug)
    form = TeamUpdateForm(instance=team)
    if request.method == 'POST':
            form = TeamUpdateForm(request.POST,  request.FILES, instance=team)
            if form.is_valid():
                form.save()
                return redirect('teams')

    context = {'form': form}
    return render(request, 'teams/team_update.html', context)
