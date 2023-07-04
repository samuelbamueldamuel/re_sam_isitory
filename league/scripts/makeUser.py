from league.models import Team
def assignUser(t_id):
    team = Team.objects.filter(t_id = t_id).first()

    team.userTeam = True  # Assign True to set the value as 1
    print(team.t_id)
    print(team.userTeam)
    team.save()
    return team