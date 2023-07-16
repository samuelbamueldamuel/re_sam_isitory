from django.core.management.base import BaseCommand, CommandParser
from league.models import Team, Player, Game
from django.db.models import Q
import random
import sys

class Command(BaseCommand):
    help = 'creates 1560 games for schedule'
    # def fun(teams):
        
    def numberedGames(self, mainTeam):
        
        list =[]
        num = 1
        for i in  range(82):
            list.append(num)
            num = num + 1
        playedGames = Game.objects.filter(Q(awayTeam=mainTeam) | Q(homeTeam=mainTeam))
        
        
        for game in playedGames:

            
            list.remove(game.week)

            # except ValueError:
            #     print(list)
            #     print(game.week)
            #     z = 0
            #     for x in list:
            #         if(list[z] == game.week):
            #             print("match found")
            #     # for x in playedGames:
            #     #     print(x.week)
            #     sys.exit()
        
        return list
    
    def checkIfThereAreDivisionGames(self, team):
        games = Game.objects.filter(Q(homeTeam=team.t_id) | Q(awayTeam=team.t_id))
        
        
        if games is None:
            return True
        else:
            return False
        
        
    def getDivOppenents(self, team ):
        div = team.division
        teams = Team.objects.filter(Q(division=div) & ~Q(t_id=team.t_id))
        return teams
    

    
    def scheduleDivOppenent(self, mainTeam, OppTeam, mainList, oppList):
        
        # print("mainTeam: " + mainTeam + "division: " + mainTeam.division)
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
        confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id))
        return confTeams
    def getGames(self, team):
        games = Game.objects.filter(Q(homeTeam=team) | Q(awayTeam=team))
        homeTeams = games.values_list('homeTeam', flat=True)
        awayTeams = games.values_list('awayTeam', flat=True)
        
    def checkConfGames(self, team):
        confTeams = self.getConfTeams(team)
        
        
        games = Game.objects.filter(Q(homeTeam=team) | Q(awayTeam=team))
        
        confTeams = Team.objects.filter(Q(conference=team.conference) & ~Q(division=team.division) & ~Q(t_id=team.t_id))
        
        
        confGamesDiv = games.filter(Q(homeTeam__conference = team.conference) | Q(awayTeam__conference = team.conference))
        confGames = confGamesDiv.filter(~Q(homeTeam__division = team.division) | ~Q(awayTeam__division = team.division))
        
        confTeamsHome = confGames.values_list('homeTeam', flat=True).distinct()
        confTeamsAway = confGames.values_list('awayTeam', flat=True).distinct()
        confTeamsPlayed = list(set(list(confTeamsHome) + list(confTeamsAway)))
        
        try:
            confTeamsPlayed.remove(team)
        except ValueError:
            pass
        
        confTeams = list(confTeams)
        for team in confTeamsPlayed:
            if team in confTeams:
                confTeams.remove(team)
                
        return confTeams
        
        
    
    def confOppenents(self, team):

        teams = self.checkConfGames(team)
        
        teamList = []
        for team in teams:
            teamList.append(team)
        sixList = []   
        for x in range(6):
            ranSixTeam = random.choice(teamList)
            sixList.append(ranSixTeam)
            teamList.remove(ranSixTeam)
        fourList = []
        for z in range(4):
            ranFourTeam = random.choice(teamList)
            fourList.append(ranFourTeam)
            teamList.remove(ranFourTeam)
            
        return sixList, fourList
    
    def schedSix(self, mainTeam, oppTeam):
        mainSched = self.numberedGames(mainTeam)   
        oppSched = self.numberedGames(oppTeam)
        print("main len: " + str(len(mainSched)))
        print("opp len: " + str(len(oppSched)))
        
        x = 0
        for x in range(4):
            gameSelectedNum = random.choice(mainSched)
            while gameSelectedNum not in oppSched:
                    gameSelectedNum = random.choice(mainSched)             
            oppSched.remove(gameSelectedNum)
            mainSched.remove(gameSelectedNum)
                
            homeOrAway = random.randint(1, 2)
                
            if(homeOrAway == 1):
                newGame = Game(homeTeam=mainTeam, awayTeam=oppTeam, week=gameSelectedNum)
                print("Home: " + newGame.homeTeam.name + "Away: " + newGame.awayTeam.name)
                newGame.save()
                x += 1
            else:
                newGame = Game(homeTeam=oppTeam, awayTeam=mainTeam, week=gameSelectedNum)
                print("Home: " + newGame.homeTeam.name + "Away: " + newGame.awayTeam.name)
                newGame.save()
                x += 1
        # print("games gend(should be 4): " + str(x) )    
    def schedFour(self, mainTeam, oppTeam):
        mainSched = self.numberedGames(mainTeam)   
        oppSched = self.numberedGames(oppTeam)
        
        mainSched = self.numberedGames(mainTeam)   
        oppSched = self.numberedGames(oppTeam)
        x = 0
        for x in range(3):
            gameSelectedNum = random.choice(mainSched)
            while gameSelectedNum not in oppSched:
                    gameSelectedNum = random.choice(mainSched)             
            oppSched.remove(gameSelectedNum)
            mainSched.remove(gameSelectedNum)
                
            homeOrAway = random.randint(1, 2)
                
            if(homeOrAway == 1):
                newGame = Game(homeTeam=mainTeam, awayTeam=oppTeam, week=gameSelectedNum)
                print("Home: " + newGame.homeTeam.name + "Away: " + newGame.awayTeam.name)
                newGame.save()
                x += 1
            else:
                newGame = Game(homeTeam=oppTeam, awayTeam=mainTeam, week=gameSelectedNum)
                print("Home: " + newGame.homeTeam.name + "Away: " + newGame.awayTeam.name)
                newGame.save()
                x += 1
        # print("games gend(should be 3)" + str(x))
        
        
        
        
    
    def genConfGames(self, team):
        sixList, fourList = self.confOppenents(team)
        print(sixList)
        print(fourList)
        
        for oppTeam in sixList:
            self.schedSix(team, oppTeam)
        for oppTeam in fourList:
            self.schedFour(team, oppTeam)
        
        
                
                
                
        
    def handle(self, *args, **kwargs):
        Game.objects.all().delete()
        teams = Team.objects.filter(~Q(t_id = 'FAA'))
        x = 0
 
        
        
        
        for team in teams:
            print(x)
            #self.genDivGames(team)
            self.genConfGames(team)
            x += 1
        # for team in teams:
        #     games = Game.objects.filter(Q(homeTeam=team) | Q(awayTeam=team)).count()
        #     print("count: " + str(games))

        
        
        
        
        
        

        # numberedGamesList = self.numberedGames()
        # areDivGames = self.checkIfThereAreDivisionGames(teams[1]) #check if theam has any scheduled games witha  division oppenent
        
        
        
        # if(areDivGames == False):
        #     divOppenents = self.getDivOppenents(teams[0])
        #     for divTeam in divOppenents:
        #         self.scheduleDivOppenent(teams[0], divTeam, numberedGamesList)
            