from django.shortcuts import render
from django.http import HttpResponse
from ..models import Team, Player

def welcome(request):
    teams = Team.objects.all()



    context = {
        'teams': teams
    }

    return render(request, 'welcome.html', context)

def home(request):
    team = Team.objects.filter(userTeam = 1).first()
    print(team.t_id)
    
    context = {
        "team": team
    }

    return render(request, 'home.html', context)

def teamRoster(request):
    team = Team.objects.filter(userTeam = True).first()

    teamPlayers = Player.objects.filter(team_id = team.t_id)

    context = {
        'team': team,
        'players': teamPlayers,
    }

    return render(request, 'teamRoster.html', context)

    