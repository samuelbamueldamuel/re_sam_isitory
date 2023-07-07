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

    teamPlayers = Player.objects.filter(team_id = team.t_id).order_by('-ovr')

    context = {
        'team': team,
        'players': teamPlayers,
    }

    return render(request, 'teamRoster.html', context)

def teams(request):
    westTeams = Team.objects.filter(conference = 'west')
    eastTeams = Team.objects.filter(conference = 'east')

    context = {
        'westTeams': westTeams,
        'eastTeams': eastTeams,
    }

    return render(request, 'teams.html', context )

def playerPage(request, id):
    selectedPlayer = Player.objects.filter(id=id).first()

    context = {
        'player': selectedPlayer
    }
    return render(request, 'playerPage.html', context)

    