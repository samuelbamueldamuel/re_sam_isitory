from django.shortcuts import render
from django.http import HttpResponse
from .scripts.gen_players import birth
from .scripts.startup_draft import rounds
from .models import Player, Team


def player(request):
    # text = generate_text()
    # number = 1
    # context = {
    #     "text": text,
    # }
    return render(request, 'players.html')

def do_shit(request):
    number = request.POST.get('num')
    num = int(number)
    for i in range(num):
        birth()
    
    
    return render(request, 'players.html')

def table(request):
    mydata = Player.objects.all().values()
    context = {
        'table': mydata,
    }
    return render(request, 'table.html', context)

def sdraft(request):
    prospects = Player.objects.filter(team_id='FA').order_by('-ovr')
    teams = Team.objects.all().exclude(id='FA')

    round = rounds(prospects, teams)
    roundx = int(round)
    roundss = range(roundx)
    i = 1
    list = []
    
        

    context = {
        'prospects': prospects,
        'teams': teams,
        'rounds': roundss,

    }

    return render(request, 'sdraft.html', context)

def ssdraft(request):
    prospects = Player.objects.filter(team_id='FA').order_by('-ovr')
    teams = Team.objects.all().exclude(id='FA')
    
    

    context = {
        'prospects': prospects
    }

    return render(request, 'sdraft.html', context)

# Create your views here.
