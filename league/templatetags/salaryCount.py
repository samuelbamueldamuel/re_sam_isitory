from django import template
from league.models import Player, Team
register = template.Library()

@register.simple_tag
def salaryCount(t_id):
    
    players = Player.objects.filter(team_id = t_id)
    
    totalSalary = 0
    
    for player in players:
        totalSalary = totalSalary + player.salary
    return totalSalary