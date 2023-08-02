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

            try:
                list.remove(game.week)
            except ValueError:
                sys.exit()

        
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
    def getConfGames(self, team):
        games = Game.objects.filter(Q(awayTeam=team) | Q(homeTeam=team))
        games = list(games)
        return games
    def playedTeams(self, team):
        games = Game.objects.filter(Q(homeTeam=team) | Q(awayTeam=team))
        
        homeTeams = games.values_list('homeTeam', flat=True).distinct()
        awayTeams = games.values_list('awayTeam', flat=True).distinct()
        
        listOfPlayed = homeTeams.union(awayTeams)
        teams = []
        
        for opp in listOfPlayed:
            teamOpp = Team.objects.filter(t_id=opp).first()
            teams.append(teamOpp)
        return teams
    
    def checkFourSix(self, team, playedTeams):
        playedTeams = list(playedTeams)
        
        if team in playedTeams:
            playedTeams.remove(team)
        
        sixList = []
        fourList = []
        
        for opp in playedTeams:
            
            gamesCount = Game.objects.filter((Q(awayTeam=team) & Q(homeTeam=opp)) | (Q(awayTeam=opp) & Q(homeTeam=team))).count()
            
            if gamesCount == 4:
                sixList.append(opp)
            elif gamesCount == 3:
                fourList.append(opp)
            elif gamesCount == 0:
                print(opp)
                print("games count was 0, why on playedTeams?")
            else:
                print("games wasnt 4 or 3")
                print(gamesCount)
        return sixList, fourList
    
    
    
    def genFourList(self, team, playedFour, playedSix, confTeams):
        
        confTeams = list(confTeams)
        for opp in playedFour:
            if opp in confTeams:
                confTeams.remove(opp)
        for opp in playedSix:
            if opp in confTeams:
                confTeams.remove(opp)
        
        teamsNeeded = 4 - len(playedFour)
        
        eligTeams = []
        fourList = []
        for opp in confTeams:
            if opp.fourTeams < 4:
                eligTeams.append(opp)
        eligLen = len(eligTeams)      
        for x in range(teamsNeeded):
            try:
                teamSel = random.choice(eligTeams)
                fourList.append(teamSel)
                eligTeams.remove(teamSel)
            except IndexError:
                sys.exit()
            
        for opp in fourList:
            opp.fourTeams += 1
            opp.save()
            
        team.fourTeams += len(fourList)
        team.save()
        
        return fourList
    
    def genSixList(self, team, playedFour, playedSix, confTeams, fourList):
        
        confTeams = list(confTeams)
        for opp in playedFour:
            if opp in confTeams:
                confTeams.remove(opp)
        for opp in playedSix:
            if opp in confTeams:
                confTeams.remove(opp)
        for opp in fourList:
            if opp in confTeams:
                confTeams.remove(opp)
        
        teamsNeeded = 6 - len(playedSix)
        
        eligTeams = []
        sixList = []
        for opp in confTeams:
            print("team: ", opp, " num: ", opp.sixTeams)
        print("confTeams", confTeams)
        for opp in confTeams:
            
            if opp.sixTeams < 6:
                eligTeams.append(opp)
            else:
                print("team: ", opp, "num: ", opp.sixTeams)
        print("eligTeams: ", eligTeams)
                
        for x in range(teamsNeeded):
            try:
                teamSel = random.choice(eligTeams)
                sixList.append(teamSel)
                eligTeams.remove(teamSel)
            except IndexError:
                sys.exit()   
        for opp in sixList:
            opp.sixTeams += 1
            opp.save()
            
        team.sixTeams += len(sixList)
        team.save()
        
        return sixList
            
        
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
    
    def genConf(self, team):
        confGames = self.getConfGames(team)
        confGames = list(confGames)

        confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id))
        
        
        playedTeams = self.playedTeams(team)
        
        
        playedSixList, playedfourList = self.checkFourSix(team, playedTeams)
        
        fourList = self.genFourList(team, playedfourList, playedSixList, confTeams)
        sixList = self.genSixList(team, playedfourList, playedSixList, confTeams, fourList)
        
        
        for opp in fourList:
            self.genFourGames(team, opp)
        for opp in sixList:
            self.genSixGames(team, opp)
        
        
        
        
        
        
        
        

    def handle(self, *args, **kwargs):
        
        #todo teams are getting scheduled for 4 games and 3 games need to fix that
        Game.objects.all().delete()
        
        teams = Team.objects.filter(~Q(t_id='FAA'))
        for teamx in teams:
            teamx.fourTeams = 0
            teamx.sixTeams = 0
            teamx.save()
        # team = Team.objects.filter(t_id='SEA').first()
        # self.genConf(team)
        for team in teams:
            self.genConf(team)
            games = Game.objects.filter(Q(homeTeam=team) | Q(awayTeam=team)).count()
            
            if games != 36:
                sys.exit()
            # self.genDivGames(team)