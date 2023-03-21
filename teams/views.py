from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from teams.models import Team, Match
from users.models import Profile


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



def team(request, slug):
    team = get_object_or_404(Team, slug=slug)
    try:
        matches = Match.objects.filter(Q(team_home=team) | Q(team_away=team))
    except:
        matches = None

    context = {'team': team, 'matches': matches}
    return render(request, 'teams/team.html', context)