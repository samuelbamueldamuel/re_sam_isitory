from django.core.management.base import BaseCommand, CommandParser
from league.models import Team, Game, Player, Record
from django.db.models import Q
import random
import sys
import time

def scheduleDivOppenent( mainTeam, OppTeam, mainList, oppList):
    oppList = list(oppList)
    mainList = list(mainList)
    
    for x in range(4):
        gameSelectedNum = random.choice(mainList)
        while gameSelectedNum not in oppList:
            gameSelectedNum = random.choice(mainList)             
        oppList.remove(gameSelectedNum)
        mainList.remove(gameSelectedNum)
        
        homeOrAway = random.randint(1, 2)
        
        if(homeOrAway == 1):
            newGame = Game(homeTeam=mainTeam, awayTeam=OppTeam, week=gameSelectedNum)
            newGame.save()
        else:
            newGame = Game(homeTeam=OppTeam, awayTeam=mainTeam, week=gameSelectedNum)
            newGame.save()
def numberedGames( mainTeam):
    
    list =[]
    num = 1
    for i in  range(82):
        list.append(num)
        num = num + 1
    playedGames = Game.objects.filter(Q(awayTeam=mainTeam) | Q(homeTeam=mainTeam))
    
    
    for game in playedGames:

        
        list.remove(game.week)

    
    return list


def checkDivGames( team):
    games = Game.objects.filter(Q(awayTeam=team) | Q(homeTeam=team))
    
    divTeams =Team.objects.filter(Q(division=team.division) & ~Q(t_id=team.t_id))
    
    divTeamsList = []
    for team in divTeams:
        divTeamsList.append(team)
    
    
    for divTeam in divTeams:
        divTeamGames = games.filter(Q(awayTeam=divTeam) | Q(homeTeam=divTeam))
        
        if not divTeamGames.exists():
            pass
        else:
            
            divTeamsList.remove(divTeam)

    return divTeamsList  

def genDivGames( team):
        divList = checkDivGames(team)
        gameList = numberedGames(team)
        
        
        for divTeam in divList:
            divGameList = numberedGames(divTeam)
            scheduleDivOppenent(team, divTeam, gameList, divGameList)    
teamsData = {}



def popDict():
    teams = Team.objects.all()
    
    numList = []
    
    x = 1
    for i in range(82):
        numList.append(x)
        x += 1
    
    for team in teams:
        
        numList = []
    
        x = 1
        for i in range(82):
            numList.append(x)
            x += 1
            
        divTeams = Team.objects.filter(Q(division = team.division) & ~Q(t_id=team.t_id))
        divTeams = list(divTeams)
        altConfTeams = Team.objects.filter(~Q(conference=team.conference) & ~Q(t_id='FAA'))
        
        altConfTeams = list(altConfTeams)
        teamsData[team.t_id] = {"fourList": [], "sixList": [], "divTeams": divTeams, "altConfTeams": altConfTeams, "games": numList}

def checkFourLen( teams):
    goodTeams = []
    for team in teams:
        teamList = teamsData[team.t_id]['fourList']
        if len(teamList) < 4:
            goodTeams.append(team)
    return goodTeams 
def getFourLens( confTeams):
    teamsDict = {}
    for team in confTeams:
        list = teamsData[team.t_id]['fourList']
        teamsDict[team.t_id] = len(list)
    return teamsDict

def backtrack( team, confTeams):
    divTeams = Team.objects.filter(Q(division=team.division) & ~Q(t_id=team.t_id))
    divTeams = list(divTeams)
    
    target = None
    for divTeam in divTeams:
        divFourList = teamsData[divTeam.t_id]['fourList']
        divFourList = list(divFourList)
        
        if len(divFourList) < 4:
            target = divTeam
    if target is None:
        print("smths fucked")
        sys.exit()
    
    
    teamSel = random.choice(confTeams)
    
    teamSelFourList = teamsData[teamSel.t_id]['fourList']
    
    for opp in teamSelFourList:
        oppOppFour = teamsData[opp.t_id]['fourList']
        
        if target not in oppOppFour:
            teamsData[teamSel.t_id]['fourList'].remove(opp)
            teamsData[opp.t_id]['fourList'].remove(teamSel)
            
            teamsData[opp.t_id]['fourList'].append(target)
            teamsData[target.t_id]['fourList'].append(opp)
            
            teamsData[team.t_id]['fourList'].append(teamSel)
            teamsData[teamSel.t_id]['fourList'].append(team)
            return
    backtrack(team, confTeams)
            
        

# def backtrack( team, confTeams):
#     teamSel = random.choice(confTeams)#random conference team, need to take one team off of fourList
#     print("team found for OG team: ", teamSel)
#     oppFourList = teamsData[teamSel.t_id]['fourList']#need to take one team off of fourList
    
    
#     secOppSel = random.choice(oppFourList)#team gonna be taken off
#     print("team found that needs to be taken off: ", secOppSel)
#     secOppConf = Team.objects.filter(Q(conference=secOppSel.conference) & ~Q(division=secOppSel.division) & ~Q(t_id=secOppSel.t_id) & ~Q(t_id=team.t_id))#looking for replacment team
#     secOppConfLen = getFourLens(secOppConf)#need to find a team with open slot
    
#     for opp in secOppConfLen: #iterating over dict to find a team with open slot
#         oppLen = secOppConfLen[opp]
#         print("searching for replacement")
#         if oppLen < 4:
#             print("replacement found: ", opp)
#             target = Team.objects.filter(t_id=opp).first()
#             teamsData[teamSel.t_id]['fourList'].remove(secOppSel)
#             teamsData[secOppSel.t_id]['fourList'].remove(teamSel)
            
#             teamsData[secOppSel.t_id]['fourList'].append(target)
#             teamsData[target.t_id]['fourList'].append(secOppSel)
            
#             teamsData[team.t_id]['fourList'].append(teamSel)
#             teamsData[teamSel.t_id]['fourList'].append(team)
#             print("ya fuckun did it")
            
#             return
#     backtrack(team, confTeams)
            
    
    
def emptyLists():
    for team in teamsData:
        teamsData[team]['fourList'].clear()
        teamsData[team]['sixList'].clear()
def emptySix():
    for team in teamsData:
        # teamsData[team]['fourList'].clear()
        teamsData[team]['sixList'].clear() 
        
def popFour( team):
    # emptyLists()
    confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id))
    confTeams = list(confTeams)
    # print("Got")
    teams = checkFourLen(confTeams)
    
    fourList = teamsData[team.t_id]['fourList']
    
    for opp in fourList:
        if opp in teams:
            teams.remove(opp)
            
    teamsNeeded = 4 - len(fourList)
    
    for x in range(teamsNeeded):
        if len(teams) == 0:
            schedConf() #todo replace this with backtrack
            return
        teamSel = random.choice(teams)
        
        teams.remove(teamSel)
        teamsData[team.t_id]['fourList'].append(teamSel)
        teamsData[teamSel.t_id]['fourList'].append(team)
        
    # print("pehraps?")
    
def popSix( team):
    
    confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id))
    confTeams = list(confTeams)
    fourList = teamsData[team.t_id]['fourList']
    
    for opp in confTeams:
        if opp not in fourList:
            teamsData[team.t_id]['sixList'].append(opp)
            # teamsData[opp.t_id]['sixList'].append(team)
    # print(len(teamsData[team.t_id]['sixList']))
    return
    
    
        
def schedConf():
    teams = Team.objects.filter(~Q(t_id='FAA'))
    emptyLists()
    for team in teams:
        popFour(team)
    emptySix()
    for team in teams:     
        popSix(team)
        
    
        
        
        
    
    # for team in teams:
    #     list = teamsData[team.t_id]['fourList']
    #     newList = teamsData[team.t_id]['sixList']
    #     print(len(list))
    #     # print(len(newList))

    # print("div done")
        
        


teamsOpps = {}

        
    
            

def popOpps():
    teams = Team.objects.filter(~Q(t_id='FAA'))     
    
    for team in teams:
        teamsOpps[team.t_id] = {}
        
        for opp in teamsData[team.t_id]['fourList']:
            teamsOpps[team.t_id][opp.t_id] = 3
        for opp in teamsData[team.t_id]['sixList']:
            teamsOpps[team.t_id][opp.t_id] = 4
        for opp in teamsData[team.t_id]['divTeams']:
            teamsOpps[team.t_id][opp.t_id] = 4
        for opp in teamsData[team.t_id]['altConfTeams']:
            teamsOpps[team.t_id][opp.t_id] = 2
            
# def getOpp( team, teams):
#     oppList = teamsOpps[team.t_id]
#     teamsList = []
#     for opp in teams:
#         teamsList.append(opp.t_id)
            
#     list = []
#     for key, value in oppList.items():
#         if value > 0:
#             list.append(key)
#     for opp in list:
        
#         if opp not in teamsList:
#             list.remove(opp)
#     oppID = random.choice(list)
#     opp = Team.objects.filter(t_id=oppID).first()
#     if opp not in teamsList:
#         pass
#     return opp

def getOpp( team, teams):
    oppList = teamsOpps[team.t_id]
    teamsList = [opp.t_id for opp in teams]
    
    valid_opponents = [opp for opp in oppList.keys() if opp in teamsList and oppList[opp] > 0]
    try:
        oppID = random.choice(valid_opponents)
    except IndexError:
        getTeamList()
    opp = Team.objects.filter(t_id=oppID).first()
    return opp
            
    
    
            
def getTeamList():
    games = {}
    teams = Team.objects.filter(~Q(t_id='FAA'))
    teams = list(teams)
    i = 1
    
        
        
    
    for x in range(15):
        teamSel = random.choice(teams)
        teams.remove(teamSel)
        length = len(teams)
        opp = getOpp(teamSel, teams)

        teams.remove(opp)
        listX = [teamSel, opp]
        games[x] = listX
    return games

def adjustOpps( dict):
    for game in dict:
        list = dict[game]
        
        teamOne = list[0]
        teamTwo = list[1]
        
        teamsOpps[teamOne.t_id][teamTwo.t_id] = teamsOpps[teamOne.t_id][teamTwo.t_id] - 1
        teamsOpps[teamTwo.t_id][teamOne.t_id] = teamsOpps[teamTwo.t_id][teamOne.t_id] - 1
        return
def schedGame( gameList, week):
    teamOne = gameList[0]
    teamTwo = gameList[1]
    
    ranNum = random.randint(1, 2)
    
    if ranNum == 1:
        newGame = Game(homeTeam=teamOne, awayTeam=teamTwo, week=week)
        newGame.save()
    if ranNum == 2:
        newGame = Game(homeTeam=teamTwo, awayTeam=teamOne, week=week )
        newGame.save()

def schedWeek( dict, week):
    for game in dict:
        gameList = dict[game]
        schedGame(gameList, week)
    
    
    
    
            
def sched():
    teams = Team.objects.filter(~Q(t_id='FAA'))
    teams = list(teams)
    weeks = []
    x = 1
    for i in range(82):
        weeks.append(x)
        x += 1
        
    for week in weeks:
        gamesDict = getTeamList()
        adjustOpps(gamesDict)
        schedWeek(gamesDict, week)
        print(week)
        
        
    
    
        
        
        
        
def createGames():
    start = time.time()
    sys.setrecursionlimit(30000)
    #TODO backtrack 
    Game.objects.all().delete()
    records = Record.objects.all()

    for record in records:
        record.wins = 0
        record.losses = 0
        record.save()


    popDict()
    teams = Team.objects.filter(~Q(t_id='FAA'))
    schedConf()
    popOpps()
    sched()
    end = time.time()
    total = end-start
    print("time: " + str(total))
    # i = 1
    # for x in games:
    #     print(games[x])
    #     i += 1
    # x = 1