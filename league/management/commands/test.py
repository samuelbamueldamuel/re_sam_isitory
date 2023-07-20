from django.core.management.base import BaseCommand, CommandParser
from league.models import Game, Team, Game
from django.db.models import Q

class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        teams = Team.objects.all()
        
        # for team in teams:
        #     games = Game.objects.filter(Q(awayTeam=team) | Q(homeTeam=team)).count()
        #     print(team.name + " game count: " + str(games))
        team = Team.objects.filter(t_id='SEA').first()
        games = Game.objects.filter(Q(awayTeam=team) | Q(homeTeam=team))
        print(len(games))
        awayTeams = games.values_list('awayTeam', flat=True).distinct()
        homeTeams = games.values_list('homeTeam', flat=True).distinct()
        
        # print(awayTeams)
        
        combined = awayTeams.union(homeTeams)
        print(awayTeams)
        print(homeTeams)
        print(combined)
        
        for oppTeam in combined:
            oppGames = games.filter(Q(awayTeam=oppTeam) | Q(homeTeam=oppTeam))
            print(oppTeam + " games: " + str(len(oppGames)))
        
        

        