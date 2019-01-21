import csv
# import os

# use letters directory
# os.chdir(r"C:\Users\Dave Fisher\Documents\GitHub\Techdegree-Project-2")
# os.mkdir('letters')


def roster_load(file, delimiter):
    # this function reads and imports the all of the soccer_players information
    with open(file, newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=delimiter)
        rows = list(player_reader)
        return rows


def roster_sort(players):
    # function creates two empty lists based off of experience
    experienced = []

    inexperienced = []

    # for loop to determine whether the player is added to either list
    for player in players:
        # if the player has no experience, add the player to the inexperienced list
        if player['Soccer Experience'] == "NO":
            inexperienced.append(player)

        # otherwise, the player must have experience, add to experienced list
        else:
            experienced.append(player)

    # return the sorted lists
    return inexperienced, experienced


def roster_teams(players, list_of_teams):
    # this function puts players into their respective teams
    # Create an index to keep track on which team each player goes to
    team_index = 0

    roster_sorted = roster_sort(players)

    # Create an empty list for all the players
    list_of_players = []

    # Create an empty list for teams
    teams = []

    # loop through the list_of_teams dictionary
    for key, value in list_of_teams.items():
        teams.append(key)
    # for loop to loop through the sorted inexperienced and experienced lists
    for sorted in roster_sorted:
        # range is the number of total teams
        range = len(teams) - 1
        # loop through the players
        for player in sorted:
            # put the player into the team at the current team_index
            player['Team'] = teams[team_index]
            # append player to the list_of_players
            list_of_players.append(player)
            # if index is less than the number of teams
            if team_index < range:
                # add 1 to the team_index
                team_index += 1
            # otherwise
            else:
                # reset the index
                team_index = 0

    return list_of_players


# function takes the populated list_of_players, and places them into the teams list
def grow_teams(teams, list_of_players):
    for player in list_of_players:
        team = player['Team']

        if team in teams:
            teams[team].append(player)

    return teams


# create the new teams.txt file with updated information
def create_team_file(teams):
    with open('teams.txt', 'a') as file:
        for team, players in teams.items():

            file.write(team + "\n")

            for player in players:

                name = player['Name']
                experience = player['Soccer Experience']
                guardian = player['Guardian Name(s)']
                file.write('{}, {}, {}\n'.format(name, experience, guardian))
            file.write('\n')


if __name__ == '__main__':
    # load in the soccer_players.csv file
    roster_load = roster_load('soccer_players.csv', ',')

    # Create a dictionary of team lists
    list_of_teams = {
        'Sharks': [],
        'Dragons': [],
        'Raptors': []
    }

    # Place players to roster_teams
    roster_teams = roster_teams(roster_load, list_of_teams)

    # Fill teams with the list_of_teams and roster_teams
    teams = grow_teams(list_of_teams, roster_teams)

    # Now generate the teams.txt file
    create_team_file(teams)




