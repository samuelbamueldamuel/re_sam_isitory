from django.shortcuts import render
from django.http import HttpResponse
from ..models import Team, Player, Game, Record
from ..scripts.stage import stage
from django.db.models import Q

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

def salaryBreakdownL(request, t_id):
    team = Team.objects.filter(t_id = t_id).first()
    
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

def teamGames(request):
    user = Team.objects.filter(userTeam=True).first()
    games = Game.objects.filter(Q(awayTeam=user) | Q(homeTeam=user))
    
    context = {
        'user': user,
        'games': games
    }
    
    return render(request, 'teamGames.html', context)

def leagueGames(request, week):
    games = Game.objects.filter(week=week)

    context = {
        'games': games
    }
    
    return render(request, 'leagueGames.html', context)

def leagueGame(request):
    number = request.POST.get('week')
    
    games = Game.objects.filter(week=number)
    print(number)
    
    context = {
        'games': games,
    }
    
    return render(request, 'leagueGames.html', context)

def standings(request):
    west = Team.objects.filter(conference='west')
    east = Team.objects.filter(conference='east')
    print(west)

    westRecord = []
    eastRecord = []

    for team in west:
        rec = Record.objects.filter(team=team).first()
        westRecord.append(rec)
    for team in east:
        rec = Record.objects.filter(team=team).first()
        eastRecord.append(rec)

    westRecord.order_by()

    context = {
        'west': west,
        'east': east,
        'westRecord': westRecord,
        'eastRecord': eastRecord,
    }
    return render(request, 'standings.html', context)


