from league.models import Team, Player

def count_pros(prospects):
    i = 0
    for prospect in prospects:
        i += 1
    return i

def count_teams(teams):
    i = 0
    for team in teams:
        i =+ 1  
    return i
    
def rounds(prospects, teams):
    for team in teams:
        id = team.id
        
    pros_len = count_pros(prospects)
    team_len = count_teams(teams)

    rounds = pros_len/team_len
    print("pp")
    return rounds 

def draft():
    prospects = Player.objects.filter(team_id='FA').order_by('-ovr').values_list('id', flat=True)
    teams = Team.objects.all().exclude(id='FA').values_list('id', flat=True)
   
    length = len(teams)

    teamLength = len(teams)
    dLen = range(len(prospects))
    
    x = 0
    draftOrder = []
    for i in dLen:
        draftOrder.append(teams[x])

        x += 1
        
        if(x == len(teams)):
            x = 0
    z = 0    
    for i in dLen:
        print("qs test:" + draftOrder[z])
        z += 1



