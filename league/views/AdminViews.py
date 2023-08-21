from django.shortcuts import render
from django.http import HttpResponse
from ..scripts.gen_players import birth
from ..scripts.startup_draft import rounds, draft, printTest
from ..scripts.makeUser import assignUser
from ..models import Player, Team, Offer, Game, Offer, PlayoffGame, PlayoffTeam, Draft
from ..scripts.delete_players import deletePlayers
from ..scripts.assignSalary import main
from ..scripts.sched import createGames
from ..scripts.assignSalary import getSalary
from ..scripts.playInit import getTeams as playoffStart
import random
from django.db.models import Q
from ..scripts.playoffEngine import main as simFirst
from ..scripts.draftOrder import order
from ..scripts.rookieGen import birth as rookieBirth


from ..scripts.engine import eng as engine
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

def cpuOffer(request, id):
    print(" you clicked that shit")
    userTeam = Team.objects.filter(userTeam=True).first()
    selectedPlayer = Player.objects.filter(id=id).first()

    user_team_id = userTeam.t_id

    # Check if offers already exist for the selected player in the database
    existing_offers = Offer.objects.filter(player=selectedPlayer)

    if not existing_offers.exists():
        # If offers don't exist in the database, generate new offers and save them
        other_teams = Team.objects.exclude(t_id=user_team_id)

        offers = []
        for team in other_teams:
            offer = {
                'team_name': team.t_id,
                'offer': getSalary(selectedPlayer.value),
            }
            offers.append(offer)

        # Save the generated offers to the database
        for offer_data in offers:
            team_name = offer_data['team_name']
            offer_value = offer_data['offer']
            offer = Offer.objects.create(team_name=team_name, offer=offer_value, player=selectedPlayer)

    else:
        # If offers exist in the database, retrieve them
        offers = [
            {'team_name': offer.team_name, 'offer': offer.offer}
            for offer in existing_offers
        ]
    
    # trying to print offer from specific team
    print(Offer.objects.filter(player_id='179',team_name = 'CTD'))
    print("OFFERS...")
    # print(offers)

    context = {
        'userTeam': userTeam,
        'player': selectedPlayer,
        'offers': offers,
    }
    return render(request, 'playersFApage.html', context)


def userOffer(request, id):
    selectedPlayer = Player.objects.filter(id=id).first()

    # Check if offers already exist for the selected player in the database
    existing_offers = Offer.objects.filter(player=selectedPlayer)

    if request.method == 'POST':
        input_offer = request.POST.get('input_offer')
        if input_offer is not None and input_offer != '':
            input_offer = float(input_offer)

            # Get the user's team to create a new offer from the user's team
            user_team = Team.objects.filter(userTeam=True).first()

            if not existing_offers.exists():
                # If offers don't exist in the database, create a new offer with user input
                offer = Offer.objects.create(
                    team_name=user_team.t_id,  # Replace with the appropriate team name from the user's team
                    offer=input_offer,
                    player=selectedPlayer,
                )
            else:
                # If offers exist in the database, update the existing offer from the user's team
                user_team_offer = existing_offers.filter(team_name=user_team.t_id).first()
                if user_team_offer:
                    user_team_offer.offer = input_offer
                    user_team_offer.save()
                else:
                    # If the user's team does not have an existing offer, create a new one
                    offer = Offer.objects.create(
                        team_name=user_team.t_id,  # Replace with the appropriate team name from the user's team
                        offer=input_offer,
                        player=selectedPlayer,
                    )

    # Retrieve the updated offers for the selected player
    updated_offers = Offer.objects.filter(player=selectedPlayer)

    context = {
        'player': selectedPlayer,
        'offers': updated_offers,
    }
    return render(request, 'playersFApage.html', context)


def faWinner(request, id):
    selectedPlayer = Player.objects.filter(id=id).first()
    # print("made it here 1")

    # Retrieve all the offers for the selected player from the database
    offers = Offer.objects.filter(player=selectedPlayer)
    # print("made it here 2")

    # Extract the offer values and corresponding team names from the queryset
    offer_values = [float(offer.offer) for offer in offers]  # Convert to float
    team_names = [offer.team_name for offer in offers]
    # print("made it here 3")

    # Apply a weight to each offer value to create a weighted random selection
    # Make sure to use consistent data types for calculations (e.g., float)
    total_offer_value = sum(offer_values)
    weights = [offer_value / total_offer_value for offer_value in offer_values]
    # print("made it here 5")

    # Use weighted random selection to determine the winnerTeam
    winner_team = random.choices(team_names, weights=weights)[0]
    # print("made it here 6")

    # Find the index of the winning team in the team_names list
    winner_team_index = team_names.index(winner_team)

    # Set the player's salary offer to the player
    selectedPlayer.salary = offer_values[winner_team_index]

    # Set the winning team's ID to the player
    selectedPlayer.team_id = winner_team  # Update with the ID of the winning team
    # print("made it here 7")

    # Save the updated selectedPlayer object to the database
    selectedPlayer.save()

    # You can now access the player's salary offer and the winning team's ID
    print("Player's Salary Offer:", selectedPlayer.salary)
    print("Winning Team's ID:", selectedPlayer.team_id)

    context = {
        'player': selectedPlayer,
        'winner_team': winner_team,
    }
    return render(request, 'playersFApage.html', context)





def makeSched(request):
    createGames()
    
    return render(request, 'home.html')

def simSeason(request):
    games = Game.objects.all()

    for game in games:
        engine(game.id)
    return render(request, 'homeSimmed.html' )

def playInit(request):
    PlayoffGame.objects.all().delete()
    PlayoffTeam.objects.all().delete()
    westGames, eastGames = playoffStart('first')

    eastFirst = PlayoffGame.objects.filter(Q(conference='east') & Q(round='first'))
    westFirst = PlayoffGame.objects.filter(Q(conference='west') & Q(round='first'))
    print(westFirst)
    print(eastFirst)
    context = {
        'westFirst': westFirst,
        'eastFirst': eastFirst,
    }

    return render(request, 'playoffTable.html', context)

def simFirstRound(request):
    simFirst('first')
    playoffStart('second')

    eastFirst = PlayoffGame.objects.filter(Q(conference='east') & Q(round='first'))
    westFirst = PlayoffGame.objects.filter(Q(conference='west') & Q(round='first'))

    eastSecond = PlayoffGame.objects.filter(Q(conference='east') & Q(round='second'))
    westSecond = PlayoffGame.objects.filter(Q(conference='west') & Q(round='second'))


    context = {
        'westFirst': westFirst,
        'eastFirst': eastFirst,
        'eastSecond': eastSecond,
        'westSecond': westSecond,
    }


    return render(request, 'playoffTable.html', context)

def simSecondRound(request):
    simFirst('second')
    playoffStart('semis')


    eastFirst = PlayoffGame.objects.filter(Q(conference='east') & Q(round='first'))
    westFirst = PlayoffGame.objects.filter(Q(conference='west') & Q(round='first'))

    eastSecond = PlayoffGame.objects.filter(Q(conference='east') & Q(round='second'))
    westSecond = PlayoffGame.objects.filter(Q(conference='west') & Q(round='second'))

    eastSemis = PlayoffGame.objects.filter(Q(conference='east') & Q(round='semis'))
    westSemis = PlayoffGame.objects.filter(Q(conference='west') & Q(round='semis'))



    context = {
        'westFirst': westFirst,
        'eastFirst': eastFirst,
        'eastSecond': eastSecond,
        'westSecond': westSecond,
        'eastSemis': eastSemis,
        'westSemis': westSemis,
    }

    return render(request, 'playoffTable.html', context)

def simSemis(request):
    simFirst('semis')
    playoffStart('finals')

    eastFirst = PlayoffGame.objects.filter(Q(conference='east') & Q(round='first'))
    westFirst = PlayoffGame.objects.filter(Q(conference='west') & Q(round='first'))

    eastSecond = PlayoffGame.objects.filter(Q(conference='east') & Q(round='second'))
    westSecond = PlayoffGame.objects.filter(Q(conference='west') & Q(round='second'))

    eastSemis = PlayoffGame.objects.filter(Q(conference='east') & Q(round='semis'))
    westSemis = PlayoffGame.objects.filter(Q(conference='west') & Q(round='semis'))
    

    finals = PlayoffGame.objects.filter(Q(round='finals')).first()


    context = {
        'westFirst': westFirst,
        'eastFirst': eastFirst,
        'eastSecond': eastSecond,
        'westSecond': westSecond,
        'eastSemis': eastSemis,
        'westSemis': westSemis,
        'finals': finals,
    }

    return render(request, 'playoffTable.html', context)

def simFinals(request):
    winner = simFirst('finals')
    print(winner)
    context = {'winner': winner}
    return render(request, 'winner.html', context)

def draftOrder(request):
    Draft.objects.all().delete()
    order()

    draftPicks = Draft.objects.all()

    context = {
        'draftPicks': draftPicks,
    }
    return render(request, 'draftOrder.html', context)

def draft(request):
    Player.objects.filter(team_id='PROS').delete()
    Draft.objects.all().delete()
    order()

    for _ in range(60):
        rookieBirth()
    
    prospects = Player.objects.filter(team_id='PROS').order_by("-ovr")
    print(prospects)
    picks = Draft.objects.all()

    context = {
        'prospects': prospects,
        'picks': picks,
    }


    return render(request, 'draft.html', context)
# Create your views here.
