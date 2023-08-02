from django.core.management.base import BaseCommand, CommandParser
from league.models import Team, Game

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('homeTeam', type=str)
        parser.add_argument('awayTeam', type=str)
        parser.add_argument('num', type=int)

    def handle(self, *args, **kwargs):
        homeTeamID = kwargs['homeTeam']
        awayTeamID = kwargs['awayTeam']
        num = kwargs['num']
        
        homeTeam = Team.objects.filter(t_id=homeTeamID).first()
        awayTeam = Team.objects.filter(t_id=awayTeamID).first()
        
        for x in range(num):
            game = Game(homeTeam=homeTeam, awayTeam=awayTeam, week=num)
            game.save()
