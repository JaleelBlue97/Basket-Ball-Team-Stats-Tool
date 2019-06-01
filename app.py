import constants

# function declarations


def clean_player_data(players):
    """Iterates through a given list of dictionaries and
    creates a new list of dictionaries with each dictionary containing altered data
    based off the data within specific key values collected during iteration. If the key
    guardians contained a string that contained the word and, that string was split into
    a list using the split method using 'and' as the splitter, and that list was stored as the new
    value for guardians. If the key experience contains the string 'yes' the boolean True is stored as the new value
    if key contained the string 'no' then store False as the new value. In all cases the height of player
    is turned into an integer value using the int() function"""

    cleaned_players = []
    for player in players:
        updated_player_info = {}
        for fields in player:
            if fields == 'name':
                updated_player_info[fields] = player[fields]
            elif fields == 'guardians':
                updated_player_info[fields] = player[fields].split("and")
            elif fields == 'experience':
                if player[fields].lower() == 'yes':
                    updated_player_info[fields] = True
                else:
                    updated_player_info[fields] = False
            elif fields == 'height':
                # uses the int function that references the string that holds the players height
                # the string is split into a list at the white space since the number appear first in each string
                # we take the value at the 0 index which is then converted into a string
                updated_player_info[fields] = int(player[fields].split()[0])
        cleaned_players.append(updated_player_info)

    return cleaned_players


def sort_players_by_experience(players):
    """Takes in a list of players and returns a tuple containing
    a two lists, one holding the experienced players and one holding the inexperienced players."""

    # uses  list comprehensions for quick list creation
    experienced_players = [player for player in players if player['experience'] is True]
    inexperienced_players = [player for player in players if player['experience'] is False]

    return experienced_players, inexperienced_players


def make_balanced_teams(players, teams = 3):
    """Takes in a list of players and sorts them into two groups
    experienced players and inexperienced players and then evenly
    distributes those players to one of three teams, each represented
    by a list. Those lists are then stored in a tuple and returned to the user."""

    potential_teams = len(players) % teams
    sorted_team = sort_players_by_experience(players)
    experienced_players = sorted_team[0]
    inexperienced_players = sorted_team[1]

    balanced_team_1 = []
    balanced_team_2 = []
    balanced_team_3 = []

    # Players are added to different teams based off the remainder of
    # index divided by potential_teams
    for index in range(0, len(experienced_players)):
        if index % potential_teams > 1:
            balanced_team_3.append(experienced_players[index])
            balanced_team_3.append(inexperienced_players[index])
        elif index % potential_teams == 1:
            balanced_team_2.append(experienced_players[index])
            balanced_team_2.append(inexperienced_players[index])
        elif index % potential_teams == 0:
            balanced_team_1.append(experienced_players[index])
            balanced_team_1.append(inexperienced_players[index])

    return balanced_team_1, balanced_team_2, balanced_team_3


PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS


basket_ball_players = []
basket_ball_teams = []

if __name__ == "__main__":
    basket_ball_players = clean_player_data(PLAYERS)
    balanced_teams = make_balanced_teams(basket_ball_players)

    print(len(balanced_teams[0]) == len(balanced_teams[1]) == len(balanced_teams[2]))
