from django.core.management.base import BaseCommand, CommandParser
from league.models import Game, Team
from django.db.models import Q

class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        team = Team.objects.all().first()
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
        
        print(list(confTeams))
        print(confTeamsPlayed)
        
        

        