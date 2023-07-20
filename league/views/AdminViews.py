from django.shortcuts import render
from django.http import HttpResponse
from ..scripts.gen_players import birth
from ..scripts.startup_draft import rounds, draft, printTest
from ..scripts.makeUser import assignUser
from ..models import Player, Team
from ..scripts.delete_players import deletePlayers
from ..scripts.assignSalary import main
import time


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
    sTime = time.time()
    for i in range(num):
        birth()
    eTime = time.time()

    execTime = str(eTime - sTime)
    execTimeInt = eTime - sTime
    timePer = execTimeInt/num

    print("Players generated:" + number)
    print("Total time taken: " + str(execTimeInt))
    print("Time per player: "  + str(timePer))

    context = {
        "playersGenerated": num,
        "execTimeInt": execTimeInt,
        "timePer": timePer,
    }
    
    return render(request, 'players.html', context)

def table(request):
    mydata = Player.objects.all().order_by('-ovr').values()
    context = {
        'table': mydata,
    }
    return render(request, 'table.html', context)

def sdraft(request):
    prospects = Player.objects.filter(team_id='FA').order_by('-ovr')
    teams = Team.objects.all().exclude(t_id='FA')

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

    return render(request, 'players.html', context)

def ssdraft(request):

    draft()
    # prospects = Player.objects.filter(team_id='FA').order_by('-ovr')
    # teams = Team.objects.all().exclude(t_id='FA')
    
    printTest()
    
    context = {
        
    }

    return render(request, 'players.html', context)



def roster(request, t_id):
    teamPlayers = Player.objects.filter(team_id=t_id).order_by('-ovr')
    team = Team.objects.filter(t_id=t_id).first()
    print(team)
    context = {
        'players': teamPlayers,
        'id': t_id,
        'team': team,
    }

    return render(request, 'roster.html', context)

def index(request):
    teams = Team.objects.all()

    context = {
        'teams': teams
    }
    return render(request, 'index.html', context)

def deletePlay(request):
    Player.objects.all().delete()


    return render(request, 'players.html')

def makeUserTeam(request, t_id):
    team = assignUser(t_id)

    context = {
        'team': team
    }

    return render(request, 'home.html', context)

def testSelTeam(request):
    obj = Team.objects.filter(userTeam = True).first()
    if obj == None:
        print("shit b roke")
    else:
        print("shit not broke")
    return render(request, 'home.html')

def assignSalary(request):
    main()
    
    return render(request, 'players.html')

def playersFA(request):
    mydata = Player.objects.filter(team_id='FAA').order_by('-ovr').values()
    context = {
        'table': mydata,
    }
    return render(request, 'playersFA.html', context)

def playersFApage(request, id):
    selectedPlayer = Player.objects.filter(id=id).first()

    context = {
        'player': selectedPlayer
    }
    return render(request, 'playersFApage.html', context)
# Create your views here.
