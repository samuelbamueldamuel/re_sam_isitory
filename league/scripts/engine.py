from league.models import Team, Game, Record, Player
import random

def getOVR(team):
    players = Player.objects.filter(team_id=team)

    

    total = 0

    for player in players:
        total = total + player.ovr

    ovr = total/len(players)

    return ovr

def getWinner(teamA, teamB):
    Aovr = getOVR(teamA)

    Bovr = getOVR(teamB)

    sum = Aovr + Bovr

    teams = [teamA, teamB]

    winner = random.choices(teams, weights=[Aovr, Bovr])
    winner = winner[0]
    print("teams: ", teams)
    # winnerIndex = teams.index(winner)
    # loser_index = 1 - winnerIndex

    if teams[0] != winner:
        loser = teams[0]
    elif teams[1] != winner:
        loser = teams[1]


    return winner, loser

def update(winner, loser, game):

    game.winner = winner
    game.loser = loser

    game.save()

    winRecord = Record.objects.filter(team=winner).first()
    winRecord.wins = winRecord.wins + 1
    winRecord.save()

    lossRecord = Record.objects.filter(team=loser).first()
    lossRecord.losses = lossRecord.losses + 1
    lossRecord.save()
    


def eng(id):
    game = Game.objects.filter(id=id).first()

    teamA = game.homeTeam
    teamB = game.awayTeam

    winner, loser = getWinner(teamA, teamB)
    update(winner, loser, game)




