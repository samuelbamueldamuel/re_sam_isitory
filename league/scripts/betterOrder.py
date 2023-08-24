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

def assignLotto(teams, i):
    
    for team in teams:
        pick = Draft(pick=i, team=team)
        pick.save()
        i += 1
    return i

def getTeams(games):
    teamsList = []

    for game in games:
        teamsList.append(game.loser)

    sortedTeams = sorted(teamsList, key=lambda team: team.record.wins, reverse=False)
    return sortedTeams
def assignFirst(teams, i):
    

    for team in teams:
        pick = Draft(pick=i, team=team)
        pick.save()
        i += 1
    return i

def assignSecond(teams, i):
    

    for team in teams:
        pick = Draft(pick=i, team=team)
        pick.save()
        i += 1
    return i
def assignSemis(teams, i):
    
    for team in teams:
        pick = Draft(pick=i, team=team)
        pick.save()
        i += 1
    return i

def makeUserpick():
    print("got")
    picks = Draft.objects.all()
    userTeam = Team.objects.filter(userTeam=True).first()
    print("user: ", userTeam)
    for pick in picks:
        # print("team: ", pick.team)
        if pick.team == userTeam:
            print("true")
            pick.userPick = True
            pick.save()


    


def order():
    i = 1
    Draft.objects.all().delete()
    for _ in range(2):
        westTeams = Team.objects.filter(conference='west').order_by('record__wins')
        eastTeams = Team.objects.filter(conference='east').order_by('record__wins')

        westLotto = getLotto(westTeams)
        eastLotto = getLotto(eastTeams)

        westLotto.extend(eastLotto)
        lottoTeams = westLotto

        sortedTeams = sorted(lottoTeams, key=lambda team: team.record.wins, reverse=False)
        i = assignLotto(sortedTeams, i)

        firstRound = PlayoffGame.objects.filter(round='first')
        sortedFirst = getTeams(firstRound)
        i = assignFirst(sortedFirst, i)

        secondRound = PlayoffGame.objects.filter(round='second')
        sortedSecond = getTeams(secondRound)
        i = assignSecond(sortedSecond, i)

        semis = PlayoffGame.objects.filter(round='semis')
        sortedSemis = getTeams(semis)
        i = assignSemis(sortedSemis, i)

        finals = PlayoffGame.objects.filter(round='finals').first()
        
        finalLoser = Draft(pick=i, team=finals.loser)
        i += 1
        finalLoser.save()
        
        finalWinner = Draft(pick=i, team=finals.winner)
        i += 1
        finalWinner.save()

    makeUserpick()