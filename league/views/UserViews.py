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

def trade(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'trade.html', context)

def tradeMachine(request, t_id):
    # get user team 
    userTeam = Team.objects.filter(userTeam=True).first()
    userPlayers = Player.objects.filter(team_id=userTeam.t_id)

    # get selectedTeam  
    selectedTeam = Team.objects.filter(t_id=t_id).first()
    selectedPlayers = Player.objects.filter(team_id=selectedTeam.t_id)
    context = {
        'userTeam': userTeam,
        'userPlayers' : userPlayers,
        'selectedTeam': selectedTeam,
        'selectedPlayers' : selectedPlayers,
        # 't_id': t_id,  # Add the t_id value to the context
    }
    print(context)
    return render(request, 'tradeMachine.html', context)





# def doTrade(request, t_id):
#     if request.method == 'POST':
#         user_player_ids = request.POST.getlist('user_players')
#         selected_player_ids = request.POST.getlist('selected_players')
        
#         try:
#             # Fetch user team and selected team
#             user_team = Team.objects.get(userTeam=True)
#             selected_team = Team.objects.get(t_id=t_id)
            
#             # Fetch the players based on the selected IDs
#             user_players = Player.objects.filter(id__in=user_player_ids, team=user_team)
#             selected_players = Player.objects.filter(id__in=selected_player_ids, team=selected_team)
            
#             # Perform the trade logic
#             # Example: Swap the teams of the selected players
#             for player in user_players:
#                 player.team = selected_team
#                 player.save()
            
#             for player in selected_players:
#                 player.team = user_team
#                 player.save()
            
#             return redirect('trade-success')
        
#         except (Team.DoesNotExist, Player.DoesNotExist):
#             # Handle the case if teams or players are not found
#             return redirect('trade-failure')
    
#     return redirect('trade-failure')

# def tradeSuccess(request):
#     return render(request, 'trade_success.html')

# def tradeFailure(request):
#     return render(request, 'trade_failure.html')