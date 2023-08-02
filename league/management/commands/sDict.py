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
                
    def schedConf(team):
        pass

   
   
   
   
    
    
    
    
    
    teamsData = {}

    
    def popDict(self):
        teams = Team.objects.all()
        
        for team in teams:
            Command.teamsData[team.t_id] = {"fourList": [], "sixList": []}
    
    
    
    
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
    
    def checkSixLen(self, teams):
        goodTeams = []
        for team in teams:
            teamList = Command.teamsData[team.t_id]['sixList']
            if len(teamList) < 6:
                goodTeams.append(team)
        return goodTeams
        
    
    def popSix(self, team, teamsLeft):
        teams = self.checkSixLen(teamsLeft)
        sixLen = len(Command.teamsData[team.t_id]['sixList'])
        teamsNeed = 6 - sixLen
        
        for x in range(teamsNeed):
            teamSel = random.choice(teams)
            teams.remove(teamSel)
            Command.teamsData[team.t_id]['sixList'].append(teamSel)
            Command.teamsData[teamSel.t_id]['sixList'].append(team)
            
    
    def checkFourLen(self, teams):
        goodTeams = []
        for team in teams:
            teamList = Command.teamsData[team.t_id]['fourList']
            if len(teamList) < 4:
                goodTeams.append(team)
        return goodTeams            
            
    def popFour(self, team, teamsLeft):
        teams = self.checkFourLen(teamsLeft)
        sixLen = len(Command.teamsData[team.t_id]['fourList'])
        teamsNeed = 4 - sixLen
        
        for x in range(teamsNeed):
            teamSel = random.choice(teams)
            teams.remove(teamSel)
            Command.teamsData[team.t_id]['fourList'].append(teamSel)
            Command.teamsData[teamSel.t_id]['fourList'].append(team)
    
        
        
        
            
        
            
    def schedConf(self, team):
        playedTeams = self.playedTeams(team)
        confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id))
        
        confTeams = list(confTeams)
        
        teamsLeft = []
        
        for opp in confTeams:
            if opp not in playedTeams:
                teamsLeft.append(opp)
                
        self.popSix(team, teamsLeft)
        
        sixList = Command.teamsData[team.t_id]['sixList']
        
        for opp in teamsLeft:
            if opp in sixList:
                teamsLeft.remove(opp)
            else:
                print("opp: ", opp)
                print(Command.teamsData[team.t_id]['sixList'])
        self.popFour(team, teamsLeft)
                
        
                
        
        
        
                
                
                
        
        
        
        
        
    def handle(self, *args, **kwargs):
        self.popDict()
        

        Game.objects.all().delete()
        
        teams = Team.objects.filter(~Q(t_id='FAA'))
        teams = list(teams)
        
        
        x = 1
        for team in teams:
            # self.genDivGames(team)
            self.schedConf(team)
            print(x)
            x += 1
            
        print("perhaps??")