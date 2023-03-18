from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from teams.models import Team, Match
from users.models import Profile


def main(request):
    matches = Match.objects.all()
    context = {'matches': matches}
    return render(request, 'main.html', context)

def users_fav_teams(request):
    profile = request.user.profile
    teams = profile.favorite_teams.all()
    # matches = Match.objects.filter(Q(team_home=teams[1]) | Q(team_away=teams[1]))
    # matches = []
    # for team in teams:
    #     matches.add(Match.objects.filter(team_home=team))
    #     matches.add(Match.objects.filter(team_away=team))
    # print(matches)
    context = {'profile': profile, 'teams': teams}
    return render(request, 'teams/users_fav_teams.html', context)

def team(request, pk):
    team = get_object_or_404(Team, id=pk)
    matches = Match.objects.filter(Q(team_home=team) | Q(team_away=team))
    print(matches)
    context = {'team': team, 'matches': matches}
    return render(request, 'teams/team.html', context)