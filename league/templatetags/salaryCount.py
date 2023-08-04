from django import template
from league.models import Player, Team, TeamSalary
register = template.Library()

@register.simple_tag
def salaryCount(t_id):
    
    players = Player.objects.filter(team_id=t_id)
    total_salary = sum(player.salary for player in players)

    # Save the total salary to the TeamSalary model
    team = Team.objects.get(t_id=t_id)
    team_salary, _ = TeamSalary.objects.get_or_create(team=team, defaults={'total_salary': total_salary})
    team_salary.total_salary = total_salary
    team_salary.save()

    return total_salary