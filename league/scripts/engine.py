from league.models import Team, Game, Record
import random

def getWinner(teamA, teamB):
    Aovr = teamA.ovr
    Bovr = teamB.ovr

    sum = Aovr + Bovr

    teams = [teamA, teamB]

    winner = random.choices(teams, weights=[Aovr, Bovr])

    teams.remove(winner)
    loser = teams[0]

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




