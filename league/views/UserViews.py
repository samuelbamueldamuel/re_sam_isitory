from django.shortcuts import render
from django.http import HttpResponse
from ..models import Team, Player
from ..scripts.stage import stage
from django.http import HttpResponse

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

# def trade(request):
#     teams = Team.objects.all()
#     context = {
#         'teams': teams
#     }
#     return render(request, 'trade.html', context)

# def tradeMachine(request, t_id):
#     # get user team 
#     userTeam = Team.objects.filter(userTeam=True).first()
#     userPlayers = Player.objects.filter(team_id=userTeam.t_id)

#     # get selectedTeam  
#     selectedTeam = Team.objects.filter(t_id=t_id).first()
#     selectedPlayers = Player.objects.filter(team_id=selectedTeam.t_id)
#     context = {
#         'userTeam': userTeam,
#         'userPlayers' : userPlayers,
#         'selectedTeam': selectedTeam,
#         'selectedPlayers' : selectedPlayers,
#         # 't_id': t_id,  # Add the t_id value to the context
#     }
#     return render(request, 'tradeMachine.html', context)

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
            'userPlayers': userPlayers,
            'selectedTeam': selectedTeam,
            'selectedPlayers': selectedPlayers,
            't_id': t_id,
        }
        return render(request, 'tradeMachine.html', context)

def addArray(request, t_id):
    user_players_list = []
    selected_players_list = []

    if request.method == 'POST':
        user_player_ids = request.POST.getlist('user_player_checkbox')
        selected_player_ids = request.POST.getlist('selected_player_checkbox')
        
        # print("user_player_ids:", user_player_ids)
        # print("selected_player_ids:", selected_player_ids)

        user_players = Player.objects.filter(id__in=user_player_ids)
        selected_players = Player.objects.filter(id__in=selected_player_ids)

        # Extend the lists with the selected players
        user_players_list.extend(user_players.values())
        selected_players_list.extend(selected_players.values())

    # Retrieve the player data for rendering the page
    userTeam = Team.objects.filter(userTeam=True).first()
    userPlayers = Player.objects.filter(team_id=userTeam.t_id).values()
    selectedTeam = Team.objects.filter(t_id=t_id).first()
    selectedPlayers = Player.objects.filter(team_id=selectedTeam.t_id).values()

    print("user_players_list:", user_players_list)
    print("selected_players_list:", selected_players_list)

    context = {
        'user_players_list': user_players_list,
        'selected_players_list': selected_players_list,
        'userPlayers': userPlayers,
        'selectedPlayers': selectedPlayers,
        't_id': t_id,
    }

    return render(request, 'tradeMachine.html', context)

def doTrade(request, t_id):
    print("DOING TRADE.........")
    user_players_list = []
    selected_players_list =  []

    if request.method == 'POST':
        print("Request method is POST")
        user_player_ids = request.POST.getlist('user_player_checkbox')
        selected_player_ids = request.POST.getlist('selected_player_checkbox')
        print("User Player IDs:", user_player_ids)
        print("Selected Player IDs:", selected_player_ids)

        # Check Player and Team models
        user_players = Player.objects.filter(id__in=user_player_ids)
        selected_players = Player.objects.filter(id__in=selected_player_ids)
        print("User Players:", user_players)
        print("Selected Players:", selected_players)

        user_players_list = list(user_players)
        selected_players_list = list(selected_players)

        # Update team IDs for user players
        userTeam = Team.objects.filter(userTeam=True).first()
        for player in user_players:
            player.team_id = t_id
            player.save()

        # Update team IDs for selected players
        for player in selected_players:
            player.team_id = userTeam.t_id
            player.save()

        print("User Players List:", user_players_list)
        print("Selected Players List:", selected_players_list)

    context = {
        'userPlayers': user_players_list,
        'selectedPlayers': selected_players_list,
        't_id': t_id,
    }

    return render(request, 'tradeMachine.html', context)




