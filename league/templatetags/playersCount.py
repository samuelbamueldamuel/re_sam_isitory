from django import template
from league.models import Player, Team

register = template.Library()

@register.simple_tag
def playersCount(t_id):
    
    
    count = Player.objects.filter(team_id = t_id).count()
    return count