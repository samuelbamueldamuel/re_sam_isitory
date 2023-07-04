from django.shortcuts import render
from django.http import HttpResponse
from ..models import Team

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

    