teams_data = {}

# Function to add a team's data
def add_team_data(team_name, four_list, six_list):
    teams_data[team_name] = {"fourList": four_list, "sixList": six_list}

# Example data for teams
team1_four_list = [1, 2, 3, 4]
team1_six_list = [10, 20, 30, 40, 50, 60]

team2_four_list = [5, 6, 7, 8]
team2_six_list = [15, 25, 35, 45, 55, 65]

# Adding data for team1 and team2
add_team_data("Team 1", team1_four_list, team1_six_list)
add_team_data("Team 2", team2_four_list, team2_six_list)

print(teams_data['Team 1']['fourList'])