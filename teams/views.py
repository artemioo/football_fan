from django.http import HttpResponse
from django.shortcuts import render

from teams.models import Teams


def main(request):
    teams = Teams.objects.all()
    context = {'teams': teams}
    return render(request, 'main.html', context)
