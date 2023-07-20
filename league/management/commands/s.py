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
    def playedTeams(self, team):
        games = Game.objects.filter(Q(homeTeam=team) | Q(awayTeam=team))
        
        homeTeams = games.values_list('homeTeam', flat=True).distinct()
        awayTeams = games.values_list('awayTeam', flat=True).distinct()
        
        listOfPlayed = homeTeams.union(awayTeams)
        teams = []
        
        for opp in listOfPlayed:
            team = Team.objects.filter(t_id=opp).first()
            teams.append(team)
        return teams
    
    def getAmountTeams(self, team, playedTeams):
        fourList = []
        sixList = [] 
        for opp in playedTeams:
            
            gamesCount = Game.objects.filter((Q(awayTeam=team) & Q(homeTeam=opp)) | (Q(awayTeam=opp) & Q(homeTeam=team))).count()
            
            
            if(gamesCount == 3):
                fourList.append(team)
            elif(gamesCount == 4):
                sixList.append(team)
            else:
                print("not six or 4, smths fucked")
            
        return fourList, sixList
    
    def genFourSixLists(self, team, playedFour, playedSix, confTeams):
        fourList = []
        sixList = []
        
        for opp in playedFour:
            fourList.append(opp)
        for opp in playedSix:
            sixList.append(opp)
            
            
        fourNeed = 4 - len(fourList)
        sixNeed = 6 - len(sixList)

        for x in range(fourNeed):
            try:
                teamSel = random.choice(confTeams)
                confTeams.remove(teamSel)
                fourList.append(teamSel)
            except IndexError:
                print("index error")
                print(team)
                gamesCount = Game.objects.filter(Q(awayTeam=team) | Q(homeTeam=team)).count()
                print(gamesCount)
                print("four: ", fourList)
                print("six: ", sixList)
                sys.exit()
                
        for x in range(sixNeed):
            try:
                teamSel = random.choice(confTeams)
                confTeams.remove(teamSel)
                sixList.append(teamSel)
            except IndexError:
                print("index error")
                print(team)
                gamesCount = Game.objects.filter(Q(awayTeam=team) | Q(homeTeam=team)).count()
                print(gamesCount)
                print("four: ", fourNeed, "   ", fourList)
                print("six: ", sixList)
                sys.exit()
            
        for opp in playedFour:
            fourList.remove(opp)
        for opp in playedSix:
            sixList.remove(opp)
            
        
            
        return fourList, sixList
            

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
        
                
    def schedConf(self, team):
        confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id)) 
        print("Team: ", team, " confTeams: ", confTeams)
        confTeams = list(confTeams) #list of objects
        playedTeams = self.playedTeams(team)
        
        for opp in playedTeams:
            if opp in confTeams:
                confTeams.remove(opp)
        
                
        playedFourList, playedSixList = self.getAmountTeams(team, playedTeams)
        
        fourList, sixList = self.genFourSixLists(team, playedFourList, playedSixList, confTeams)
        
        
        for opp in fourList:
            self.genFourGames(team, opp)
        for opp in sixList:
            self.genSixGames(team, opp)
        
        
        
        
        
        
        
        
        


    def handle(self, *args, **kwargs):
        Game.objects.all().delete()
    
        teams = Team.objects.filter(~Q(t_id='FAA'))
        # team = teams.first()
        # self.schedConf(team)
        for team in teams:
            # self.genDivGames(team)
            self.schedConf(team)