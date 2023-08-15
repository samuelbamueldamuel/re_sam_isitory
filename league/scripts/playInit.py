from league.models import Team, PlayoffGame, PlayoffTeam
# def seed(teams):
#     dict = {}

#     teams = list(teams)

#     i = 0
#     x = 1

#     while i != 8:
#         dict[x] = teams[i]
#         i += 1
#         x += 1

#     return dict

def seedTeams(teams):
    x = 1
    for team in teams:
        if x == 9:
            return
        instance = PlayoffTeam(seed=x, team=team, conference=team.conference)
        instance.save()
        x += 1





# def createMatchups(teams):
     
#     games = len(teams)/2
#     games = int(games)

#     seeds = teams.keys()
#     seeds = list(seeds)
#     gamesList = []
    
#     for x in range(games):
#         top = min(seeds)
#         bottom = max(seeds)
#         game = PlayoffGame(homeTeam=teams[top], awayTeam=teams[bottom])
#         game.save()
#         gamesList.append(game)
#         seeds.remove(top)
#         seeds.remove(bottom)
#     return gamesList
def sched(seeded, gamesAmount, round):
    seeds = seeded.keys()
    seeds = list(seeds)
    gamesList = []
    for _ in range(gamesAmount):
        top = min(seeds)
        bottom = max(seeds)
        game = PlayoffGame(homeTeam=seeded[top].team, awayTeam=seeded[bottom].team, conference=seeded[top].conference, round=round)
        game.save()
        gamesList.append(game)
        seeds.remove(top)
        seeds.remove(bottom)
    return gamesList




def createMatchups(round):
    eastTeams = PlayoffTeam.objects.filter(conference='east').order_by('seed')
    westTeams = PlayoffTeam.objects.filter(conference='west').order_by('seed')

    eastTeams, westTeams = list(eastTeams), list(westTeams)

    gamesAmount = len(eastTeams)/2

    gamesAmount = int(gamesAmount)
    eastSeed = {}
    for team in eastTeams:
        eastSeed[team.seed] = team
    westSeed = {}
    for team in westTeams:
        westSeed[team.seed] = team

    eastGames, westGames = sched(eastSeed, gamesAmount, round), sched(westSeed, gamesAmount, round)
    return eastGames, westGames



        
        




def getTeams(round):
    if round == 'finals':
        eastTeam = PlayoffTeam.objects.filter(conference='east').first()
        westTeam = PlayoffTeam.objects.filter(conference='west').first()
        game = PlayoffGame(homeTeam=westTeam.team, awayTeam=eastTeam.team, conference='fin', round=round)
        game.save()
        


    westTeams = Team.objects.filter(conference='west').order_by('-record__wins')
    eastTeams = Team.objects.filter(conference='east').order_by('-record__wins')
    if round == 'first':
        seedTeams(westTeams)
        seedTeams(eastTeams)

    eastGames, westGames = createMatchups(round)

    return westGames, eastGames


