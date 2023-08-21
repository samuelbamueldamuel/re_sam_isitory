from league.models import Team, Draft, PlayoffGame
def getLotto(teams):
    i = 1
    teamList = []
    for team in teams:
        if i == 8:
            return teamList

        teamList.append(team)
        i += 1

# def orderLotto(teams):
#     i = 1

#     for team in teams:

def assignLotto(teams):
    i = 1
    for team in teams:
        pick = Draft(pick=i, team=team)
        pick.save()
        i += 1

def getTeams(games):
    teamsList = []

    for game in games:
        teamsList.append(game.loser)

    sortedTeams = sorted(teamsList, key=lambda team: team.record.wins, reverse=False)
    return sortedTeams
def assignFirst(teams):
    i = 15

    for team in teams:
        pick = Draft(pick=i, team=team)
        pick.save()
        i += 1

def assignSecond(teams):
    i = 23

    for team in teams:
        pick = Draft(pick=i, team=team)
        pick.save()
        i += 1
def assignSemis(teams):
    i = 27
    for team in teams:
        pick = Draft(pick=i, team=team)
        pick.save()
        i += 1

    


def order():
    Draft.objects.all().delete()
    for _ in range(2):
        westTeams = Team.objects.filter(conference='west').order_by('record__wins')
        eastTeams = Team.objects.filter(conference='east').order_by('record__wins')

        westLotto = getLotto(westTeams)
        eastLotto = getLotto(eastTeams)

        westLotto.extend(eastLotto)
        lottoTeams = westLotto

        sortedTeams = sorted(lottoTeams, key=lambda team: team.record.wins, reverse=False)
        assignLotto(sortedTeams)

        firstRound = PlayoffGame.objects.filter(round='first')
        sortedFirst = getTeams(firstRound)
        assignFirst(sortedFirst)

        secondRound = PlayoffGame.objects.filter(round='second')
        sortedSecond = getTeams(secondRound)
        assignSecond(sortedSecond)

        semis = PlayoffGame.objects.filter(round='semis')
        sortedSemis = getTeams(semis)
        assignSemis(sortedSemis)

        finals = PlayoffGame.objects.filter(round='finals').first()
        finalLoser = Draft(pick=29, team=finals.loser)
        finalLoser.save()
        finalWinner = Draft(pick=30, team=finals.winner)
        finalWinner.save()


    
    

