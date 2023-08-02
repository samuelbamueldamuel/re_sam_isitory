from django.core.management.base import BaseCommand, CommandParser
from league.models import Team, Player, Game
from django.db.models import Q
import random


class Command(BaseCommand):
    help = "things"

    def handle(self, *args, **kwargs):
        teams = Team.objects.filter(~Q(t_id='FAA'))
        
        for team in teams:
            div = team.division
            
            divTeams = Team.objects.filter(Q(division = div) & ~Q(t_id = team.t_id))
            
            
            schedule = []
            x = 1
            for x in range(1, 83):
                schedule.append(x)
                
            for divTeam in divTeams:
                x = 1
                games = []
                for l in range(x):
                    gamesNum = random.choice(schedule)
                    games.append(gamesNum)
                print("div accum: " + str(x))
                x = x + 1
                for z in range(4):
                    print(games)
                    print("team working: " + team.name +"game selected: " + str(games[z]) + "division: " + team.division + "accum num: " + str(z))
                    
                    schedule.remove(games[z])
                    
                    
                    homeOrAway = random.randint(1, 2)
                    
                    if(homeOrAway == 1):
                        newGame = Game(homeTeam=team, awayTeam=divTeam, week=games[z])
                        newGame.save()
                
            
            
            
            
            