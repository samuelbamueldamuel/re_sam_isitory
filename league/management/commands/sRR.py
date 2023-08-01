from django.core.management.base import BaseCommand, CommandParser
from league.models import Team, Game, Player
from django.db.models import Q
import random
import sys
import time
class Command(BaseCommand):
    def scheduleDivOppenent(self, mainTeam, OppTeam, mainList, oppList):
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
    def numberedGames(self, mainTeam):
        
        list =[]
        num = 1
        for i in  range(82):
            list.append(num)
            num = num + 1
        playedGames = Game.objects.filter(Q(awayTeam=mainTeam) | Q(homeTeam=mainTeam))
        
        
        for game in playedGames:

            
            list.remove(game.week)

        
        return list
    
    
    def checkDivGames(self, team):
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
    
    def genDivGames(self, team):
            divList = self.checkDivGames(team)
            gameList = self.numberedGames(team)
            
            
            for divTeam in divList:
                divGameList = self.numberedGames(divTeam)
                self.scheduleDivOppenent(team, divTeam, gameList, divGameList)    
    teamsData = {}
    
    
    
    def popDict(self):
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
            Command.teamsData[team.t_id] = {"fourList": [], "sixList": [], "divTeams": divTeams, "altConfTeams": altConfTeams, "games": numList}

    def checkFourLen(self, teams):
        goodTeams = []
        for team in teams:
            teamList = Command.teamsData[team.t_id]['fourList']
            if len(teamList) < 4:
                goodTeams.append(team)
        return goodTeams 
    def getFourLens(self, confTeams):
        teamsDict = {}
        for team in confTeams:
            list = Command.teamsData[team.t_id]['fourList']
            teamsDict[team.t_id] = len(list)
        return teamsDict
    
    def backtrack(self, team, confTeams):
        divTeams = Team.objects.filter(Q(division=team.division) & ~Q(t_id=team.t_id))
        divTeams = list(divTeams)
        
        target = None
        for divTeam in divTeams:
            divFourList = Command.teamsData[divTeam.t_id]['fourList']
            divFourList = list(divFourList)
            
            if len(divFourList) < 4:
                target = divTeam
        if target is None:
            print("smths fucked")
            sys.exit()
        
        
        teamSel = random.choice(confTeams)
        
        teamSelFourList = Command.teamsData[teamSel.t_id]['fourList']
        
        for opp in teamSelFourList:
            oppOppFour = Command.teamsData[opp.t_id]['fourList']
            
            if target not in oppOppFour:
                Command.teamsData[teamSel.t_id]['fourList'].remove(opp)
                Command.teamsData[opp.t_id]['fourList'].remove(teamSel)
                
                Command.teamsData[opp.t_id]['fourList'].append(target)
                Command.teamsData[target.t_id]['fourList'].append(opp)
                
                Command.teamsData[team.t_id]['fourList'].append(teamSel)
                Command.teamsData[teamSel.t_id]['fourList'].append(team)
                return
        self.backtrack(team, confTeams)
                
            
    
    # def backtrack(self, team, confTeams):
    #     teamSel = random.choice(confTeams)#random conference team, need to take one team off of fourList
    #     print("team found for OG team: ", teamSel)
    #     oppFourList = Command.teamsData[teamSel.t_id]['fourList']#need to take one team off of fourList
        
        
    #     secOppSel = random.choice(oppFourList)#team gonna be taken off
    #     print("team found that needs to be taken off: ", secOppSel)
    #     secOppConf = Team.objects.filter(Q(conference=secOppSel.conference) & ~Q(division=secOppSel.division) & ~Q(t_id=secOppSel.t_id) & ~Q(t_id=team.t_id))#looking for replacment team
    #     secOppConfLen = self.getFourLens(secOppConf)#need to find a team with open slot
        
    #     for opp in secOppConfLen: #iterating over dict to find a team with open slot
    #         oppLen = secOppConfLen[opp]
    #         print("searching for replacement")
    #         if oppLen < 4:
    #             print("replacement found: ", opp)
    #             target = Team.objects.filter(t_id=opp).first()
    #             Command.teamsData[teamSel.t_id]['fourList'].remove(secOppSel)
    #             Command.teamsData[secOppSel.t_id]['fourList'].remove(teamSel)
                
    #             Command.teamsData[secOppSel.t_id]['fourList'].append(target)
    #             Command.teamsData[target.t_id]['fourList'].append(secOppSel)
                
    #             Command.teamsData[team.t_id]['fourList'].append(teamSel)
    #             Command.teamsData[teamSel.t_id]['fourList'].append(team)
    #             print("ya fuckun did it")
                
    #             return
    #     self.backtrack(team, confTeams)
                
        
        
    def emptyLists(self):
        for team in Command.teamsData:
            Command.teamsData[team]['fourList'].clear()
            Command.teamsData[team]['sixList'].clear()
    def emptySix(self):
        for team in Command.teamsData:
            # Command.teamsData[team]['fourList'].clear()
            Command.teamsData[team]['sixList'].clear() 
            
    def popFour(self, team):
        # self.emptyLists()
        confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id))
        confTeams = list(confTeams)
        # print("Got")
        teams = self.checkFourLen(confTeams)
        
        fourList = Command.teamsData[team.t_id]['fourList']
        
        for opp in fourList:
            if opp in teams:
                teams.remove(opp)
                
        teamsNeeded = 4 - len(fourList)
        
        for x in range(teamsNeeded):
            if len(teams) == 0:
                self.schedConf() #todo replace this with backtrack
                return
            teamSel = random.choice(teams)
            
            teams.remove(teamSel)
            Command.teamsData[team.t_id]['fourList'].append(teamSel)
            Command.teamsData[teamSel.t_id]['fourList'].append(team)
            
        # print("pehraps?")
        
    def popSix(self, team):
        
        confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id))
        confTeams = list(confTeams)
        fourList = Command.teamsData[team.t_id]['fourList']
        
        for opp in confTeams:
            if opp not in fourList:
                Command.teamsData[team.t_id]['sixList'].append(opp)
                # Command.teamsData[opp.t_id]['sixList'].append(team)
        # print(len(Command.teamsData[team.t_id]['sixList']))
        return
        
        
           
    def schedConf(self):
        teams = Team.objects.filter(~Q(t_id='FAA'))
        self.emptyLists()
        for team in teams:
            self.popFour(team)
        self.emptySix()
        for team in teams:     
            self.popSix(team)
            
        
            
            
            
        
        # for team in teams:
        #     list = Command.teamsData[team.t_id]['fourList']
        #     newList = Command.teamsData[team.t_id]['sixList']
        #     print(len(list))
        #     # print(len(newList))

        # print("div done")
            
            
   
    
    teamsOpps = {}
    
            
        
                

    def popOpps(self):
        teams = Team.objects.filter(~Q(t_id='FAA'))     
        
        for team in teams:
            Command.teamsOpps[team.t_id] = {}
            
            for opp in Command.teamsData[team.t_id]['fourList']:
                Command.teamsOpps[team.t_id][opp.t_id] = 3
            for opp in Command.teamsData[team.t_id]['sixList']:
                Command.teamsOpps[team.t_id][opp.t_id] = 4
            for opp in Command.teamsData[team.t_id]['divTeams']:
                Command.teamsOpps[team.t_id][opp.t_id] = 4
            for opp in Command.teamsData[team.t_id]['altConfTeams']:
                Command.teamsOpps[team.t_id][opp.t_id] = 2
                
    # def getOpp(self, team, teams):
    #     oppList = Command.teamsOpps[team.t_id]
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
    
    def getOpp(self, team, teams):
        oppList = Command.teamsOpps[team.t_id]
        teamsList = [opp.t_id for opp in teams]
        
        valid_opponents = [opp for opp in oppList.keys() if opp in teamsList and oppList[opp] > 0]
        try:
            oppID = random.choice(valid_opponents)
        except IndexError:
            self.getTeamList()
        opp = Team.objects.filter(t_id=oppID).first()
        return opp
                
        
        
                
    def getTeamList(self):
        games = {}
        teams = Team.objects.filter(~Q(t_id='FAA'))
        teams = list(teams)
        i = 1
        
            
            
        
        for x in range(15):
            teamSel = random.choice(teams)
            teams.remove(teamSel)
            length = len(teams)
            opp = self.getOpp(teamSel, teams)

            teams.remove(opp)
            listX = [teamSel, opp]
            games[x] = listX
        return games
    
    def adjustOpps(self, dict):
        for game in dict:
            list = dict[game]
            
            teamOne = list[0]
            teamTwo = list[1]
            
            Command.teamsOpps[teamOne.t_id][teamTwo.t_id] = Command.teamsOpps[teamOne.t_id][teamTwo.t_id] - 1
            Command.teamsOpps[teamTwo.t_id][teamOne.t_id] = Command.teamsOpps[teamTwo.t_id][teamOne.t_id] - 1
            return
    def schedGame(self, gameList, week):
        teamOne = gameList[0]
        teamTwo = gameList[1]
        
        ranNum = random.randint(1, 2)
        
        if ranNum == 1:
            newGame = Game(homeTeam=teamOne, awayTeam=teamTwo, week=week)
            newGame.save()
        if ranNum == 2:
            newGame = Game(homeTeam=teamTwo, awayTeam=teamOne, week=week )
            newGame.save()
    
    def schedWeek(self, dict, week):
        for game in dict:
            gameList = dict[game]
            self.schedGame(gameList, week)
        
        
        
        
                
    def sched(self):
        teams = Team.objects.filter(~Q(t_id='FAA'))
        teams = list(teams)
        weeks = []
        x = 1
        for i in range(82):
            weeks.append(x)
            x += 1
            
        for week in weeks:
            gamesDict = self.getTeamList()
            self.adjustOpps(gamesDict)
            self.schedWeek(gamesDict, week)
            print(week)
            
            
        
        
            
            
            
            
    def handle(self, *args, **kwargs):
        start = time.time()
        sys.setrecursionlimit(30000)
        #TODO backtrack 
        Game.objects.all().delete()
        self.popDict()
        teams = Team.objects.filter(~Q(t_id='FAA'))
        self.schedConf()
        self.popOpps()
        self.sched()
        end = time.time()
        total = end-start
        print("time: " + str(total))
        # i = 1
        # for x in games:
        #     print(games[x])
        #     i += 1
        # x = 1
