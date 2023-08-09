from django.core.management.base import BaseCommand, CommandParser
from league.models import Team, Record

class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        teams = Team.objects.all()

        for team in teams:
            instance = Record(team=team)
            instance.save()


