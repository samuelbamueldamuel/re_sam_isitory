from django.core.management.base import BaseCommand, CommandParser
from league.models import Player

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        obj = Player.objects.get(id=2048)
        obj.team_id = 'COB'
        obj.save()
        obj = Player.objects.get(id=2048)
        print(obj.team_id)
        