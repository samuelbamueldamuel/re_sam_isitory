from league.models import Player


def deletePlayers():
    Player.objects.all().delete()



