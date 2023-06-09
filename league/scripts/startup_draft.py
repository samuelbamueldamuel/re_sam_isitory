

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
        print(id)
    pros_len = count_pros(prospects)
    team_len = count_teams(teams)

    rounds = pros_len/team_len
    print("pp")
    return rounds 

