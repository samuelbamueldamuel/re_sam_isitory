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

    
    def getConfTeams(self, team):
        confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division))
        return confTeams
    
    def checkNumGames(self, team, opp):
        games = Game.objects.filter((Q(awayTeam=team) & Q(homeTeam=opp)) | (Q(awayTeam=opp) & Q(homeTeam=team))).count()
        return games
    
    def checkFourGames(self, team):
        games = Game.objects.filter(Q(awayTeam=team) | Q(homeTeam=team))
        
        homeTeams = games.values_list('homeTeam', flat=True).distinct()
        awayTeams = games.values_list('awayTeam', flat=True).distinct()
        
        listOfPlayed = homeTeams.union(awayTeams)
        fourList = []
        for played in listOfPlayed:
            numGamesPlayed = self.checkNumGames(team, played)
            if(numGamesPlayed == 4):
                fourList.append(played)
        return fourList
            
    def checkSixGames(self, team):
        games = Game.objects.filter(Q(awayTeam=team) | Q(homeTeam=team))
        
        homeTeams = games.values_list('homeTeam', flat=True).distinct()
        awayTeams = games.values_list('awayTeam', flat=True).distinct()
        
        listOfPlayed = homeTeams.union(awayTeams)
        sixList = []
        for played in listOfPlayed:
            numGamesPlayed = self.checkNumGames(team, played)
            if(numGamesPlayed == 6):
                sixList.append(played)
        return sixList           
    
    
    def getFourList(self, team, confTeams, playedFour):
        confTeams = list(confTeams)
        
        fourList = []
        for opp in playedFour:
            fourList.append(opp)
            
        length = len(fourList)
        need = 4-length
        
        for x in range(need):
            ranTeam = random.choice(confTeams)
            confTeams.remove(ranTeam)
            
            fourList.append(ranTeam)
        return fourList
            
    def getSixList(self, team, confTeams, playedFour):
        confTeams = list(confTeams)
        
        sixList = []
        for opp in playedFour:
            sixList.append(opp)
            
        length = len(sixList)
        need = 4-length
        
        for x in range(need):
            ranTeam = random.choice(confTeams)
            confTeams.remove(ranTeam)
            
            sixList.append(ranTeam)
        return sixList
    
    def genSixGames(self, mainTeam, oppTeam):
        mainSched = self.numberedGames(mainTeam)
        oppSched = self.numberedGames(oppTeam)
        
        mainSched = set(mainSched)
        oppSched = set(oppSched)
        
        games = list(mainSched.intersection(oppSched))[:6]
        games = list(games)
        
        for x in games:
            homeOrAway = random.randint(1, 2)
                
            if(homeOrAway == 1):
                
                newGame = Game(homeTeam=mainTeam, awayTeam=oppTeam, week=x)
                
                newGame.save()
                
            else:
                
                newGame = Game(homeTeam=oppTeam, awayTeam=mainTeam, week=x)
                
                newGame.save()
                
    def genFourGames(self, mainTeam, oppTeam):
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
        
        

        
    
    def genConfGames(self, team):
        confTeams = self.getConfTeams(team)
        confTeams = list(confTeams)
        
        playedFourGames = self.checkFourGames(team)
        playedSixGames = self.checkSixGames(team)
        
        fourList = self.getFourList(team, confTeams, playedFourGames)
        
        # newConfTeams = [x for x in confTeams if x not in fourList]  #removes every team fron confTeam that is in fourList
        newConfTeams = confTeams
        
        
        
        for opp in fourList:
            if opp in newConfTeams:
                newConfTeams.remove(opp)
            
        
        sixList = self.getSixList(team, newConfTeams, playedSixGames)
        
        # newFourList = [x for x in fourList if x not in playedFourGames]
        
        newFourList = fourList
        for opp in playedFourGames:
            if opp in newFourList:
                newFourList.remove(opp)
        
        
        
        
        # newSixList = [x for x in sixList if x not in playedSixGames]
        newSixList = sixList
        
        for opp in playedSixGames:
            if opp in newSixList:
                newSixList.remove(opp)
        print("teamBeingSched: ", team)
                
        print("fourList: ", fourList)
        
        print("newFourList: ", newFourList)
        print("sixList: ", sixList)
        print("newSixList: ", newSixList)
        
        for opp in newFourList:
            self.genFourGames(team, opp)
        for opp in newSixList:
            self.genSixGames(team, opp)
        
        
        
        
    
    
    def handle(self, *args, **kwargs):
        # Game.objects.all().delete()
        
        # teams = Team.objects.filter(~Q(t_id='FAA'))
        
        # for team in teams:
        #     self.genConfGames(team)
        
        team = Team.objects.filter(t_id='ATH').first()
        list = self.checkFourGames(team)
        print(list)
            
            
            # self.genDivGames(team)
       