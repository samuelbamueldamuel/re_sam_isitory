from django.core.management.base import BaseCommand, CommandParser
from league.models import Team, Game, Player
from django.db.models import Q
import random
import sys

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
        
        for team in teams:
            Command.teamsData[team.t_id] = {"fourList": [], "sixList": []}

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
        print("Got")
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
            
        print("pehraps?")
        
    def popSix(self, team):
        
        confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id))
        confTeams = list(confTeams)
        fourList = Command.teamsData[team.t_id]['fourList']
        
        for opp in confTeams:
            if opp not in fourList:
                Command.teamsData[team.t_id]['sixList'].append(opp)
                # Command.teamsData[opp.t_id]['sixList'].append(team)
        print(len(Command.teamsData[team.t_id]['sixList']))
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
    def genFourGames(self, mainTeam, oppTeam):
        mainSched = self.numberedGames(mainTeam)
        oppSched = self.numberedGames(oppTeam)
        
        mainSched = set(mainSched)
        oppSched = set(oppSched)
        
        games = list(mainSched.intersection(oppSched))[:3]
        games = list(games)
        
        for x in games:
            homeOrAway = random.randint(1, 2)
                
            if(homeOrAway == 1):
                
                newGame = Game(homeTeam=mainTeam, awayTeam=oppTeam, week=x)
                
                newGame.save()
                
            else:
                
                newGame = Game(homeTeam=oppTeam, awayTeam=mainTeam, week=x)
                
                newGame.save()
                

    def genSixGames(self, mainTeam, oppTeam):
        mainSched = self.numberedGames(mainTeam)
        oppSched = self.numberedGames(oppTeam)
        
        mainSched = set(mainSched)
        oppSched = set(oppSched)
        
        games = list(mainSched.intersection(oppSched))[:4]
        games = list(games)
        
        for x in games:
            homeOrAway = random.randint(1, 2)
                
            if(homeOrAway == 1):
                
                newGame = Game(homeTeam=mainTeam, awayTeam=oppTeam, week=x)
                
                newGame.save()
                
            else:
                
                newGame = Game(homeTeam=oppTeam, awayTeam=mainTeam, week=x)
                
                newGame.save()    
                        
    def genConf(self):
        teams = Team.objects.filter(~Q(t_id='FAA'))
        
        for team in teams:
            fourList = Command.teamsData[team.t_id]['fourList']
            for opp in fourList:
                self.genFourGames(team, opp)
                Command.teamsData[opp.t_id]['fourList'].remove(team)
        for team in teams:
            sixList = Command.teamsData[team.t_id]['sixList']
            for opp in sixList:
                self.genSixGames(team, opp)
                Command.teamsData[opp.t_id]['sixList'].remove(team)             
            
            
    def handle(self, *args, **kwargs):
        sys.setrecursionlimit(30000)
        #TODO backtrack 
        Game.objects.all().delete()
        self.popDict()
        teams = Team.objects.filter(~Q(t_id='FAA'))
        self.schedConf()
        self.genConf()
        # for team in teams:
        #     self.genDivGames(team)