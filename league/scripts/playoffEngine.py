from league.models import PlayoffGame, PlayoffTeam, Team, Player
import random

def getOVR(team):
    players = Player.objects.filter(team_id=team)

    

    total = 0

    for player in players:
        total = total + player.ovr

    ovr = total/len(players)

    return ovr


def simGame(game):
    teamA = game.homeTeam

    teamB = game.awayTeam

    Aovr = getOVR(teamA)
    Bovr = getOVR(teamB)

    teams = [teamA, teamB]

    winner = random.choices(teams, weights=[Aovr, Bovr])
    winner = winner[0]
    # print("teams: ", teams)
    # winnerIndex = teams.index(winner)
    # loser_index = 1 - winnerIndex

    if teams[0] != winner:
        loser = teams[0]
    elif teams[1] != winner:
        loser = teams[1]


    return winner, loser




def main(round):
    games = PlayoffGame.objects.filter(round=round)

    for game in games:
        winner, loser = simGame(game)
        loserTeam = PlayoffTeam.objects.filter(team=loser).first()
        print(loserTeam)
        loserTeam.delete()
    return winner
        


