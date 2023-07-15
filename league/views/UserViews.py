from django.shortcuts import render
from django.http import HttpResponse
from ..models import Team, Player
from ..scripts.stage import stage

def welcome(request):
    teams = Team.objects.all()



    context = {
        'teams': teams
    }

    return render(request, 'welcome.html', context)

def home(request):
    team = Team.objects.filter(userTeam = 1).first()
    print(team.t_id)
    
    leagueStage = stage
    
    context = {
        "team": team,
        "stage": stage,
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

def salaryBreakdown(request):
    team = Team.objects.filter(userTeam = True).first()
    
    players = Player.objects.filter(team_id = team.t_id)
    
    totalSalary = 0
    for player in players:
        totalSalary = totalSalary + player.salary
        
    
    context = {
        'team': team,
        'players': players,
        'totalSalary': totalSalary,
    }
    
    return render(request, 'salaryBreakdown.html', context)

def leagueSalary(request):
    
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    firstTeam = teams[3]
    print(firstTeam.name)
    
    for team in teams:
        players = Player.objects.filter(team_id = team.t_id)
        teamSalary = 0
        for player in players:
            teamSalary = teamSalary + player.salary

        key = team.t_id + 'Salary'  
        context[key] = teamSalary    
        
        count = Player.objects.filter(team_id = team.t_id).count()
        playerKey = team.t_id + 'Players'
        
        
        context[playerKey] = count
    print(context['LASPlayers'])
        
    
    return render(request, 'leagueSalary.html', context)

def testView(request):
    context = {
        'key': 'value'
    }
    return render(request, 'test.html', context)

def trade(request, t_id):
    context = {
        'key': 'value'
    }
    return render(request, 'tradeMachine.html', context)