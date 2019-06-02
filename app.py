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
                individual_guardians = player[fields].split("and")
                updated_player_info[fields] = [guardian.strip() for guardian in individual_guardians]
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

    sorted_team = sort_players_by_experience(players)
    experienced_players = sorted_team[0]
    inexperienced_players = sorted_team[1]

    balanced_team_1 = []
    balanced_team_2 = []
    balanced_team_3 = []

    # Players are added to different teams based off the remainder of
    # index divided by potential_teams
    for index in range(0, len(experienced_players)):
        if index % teams > 1:
            balanced_team_3.append(experienced_players[index])
            balanced_team_3.append(inexperienced_players[index])
        elif index % teams == 1:
            balanced_team_2.append(experienced_players[index])
            balanced_team_2.append(inexperienced_players[index])
        elif index % teams == 0:
            balanced_team_1.append(experienced_players[index])
            balanced_team_1.append(inexperienced_players[index])

    return balanced_team_1, balanced_team_2, balanced_team_3


def get_average_height(team):
    """Returns the average height of the players on the team"""
    total_height = 0
    for player in team:
        total_height += player['height']

    return total_height / len(team)


def test_input(user_input):
    """Tests a given input and returns that input if it can turned into an int"""
    try:
        int(user_input)
    except ValueError:
        return "\nThat wasn't a valid input"
    else:
        return int(user_input)


def menu_one(teams, team_names):
    """Displays the first menu of the app"""
    interface_heading = "\nBASKETBALL TEAM STATS TOOL\n"
    menu = "-----Menu------"
    user_options = """\nHere are your choices:\n 1) Display Team Stats\n 2) Quit"""
    user_prompt = "\nEnter an option > "

    display_team = """\n1) {}\n2) {}\n3) {}""".format(team_names[0],
                                                 team_names[1], team_names[2])

    using_app = True

    print(interface_heading)
    print(menu)
    print(user_options)

    user_menu_selection = input(user_prompt)

    """
    Tests the users given input and calls menu_two if the correct input was given
    if the correct input was not given then an error message is given and 
    menu_one is called again."""
    try:
        user_menu_selection = test_input(int(user_menu_selection))

    except ValueError:
        print(user_menu_selection)
        menu_one(teams, team_names)

    else:
        if user_menu_selection != 1 and user_menu_selection != 2:
            print("\nPlease select choose option 1) or 2)")
            menu_one(teams, team_names)

    if user_menu_selection == 1:
        menu_two(teams, team_names)


def menu_two(teams, team_names):
    """Displays menu 2 and allows the user to select a
    team and bring them to the screen that allows them to screen view the stats of that team"""
    user_prompt = "\nEnter an option > "

    display_team = """\n1) {}\n2) {}\n3) {}""".format(team_names[0],
                                                 team_names[1], team_names[2])

    print(display_team)
    user_menu_selection = input(user_prompt)
    try:
        user_menu_selection2 = test_input(int(user_menu_selection))
    except ValueError:
        print(user_menu_selection2)
        menu_two(teams, team_names)
    else:
        if user_menu_selection2 != 1 and user_menu_selection2 != 2 and user_menu_selection2 != 3:
            print("\nPlease select choose option 1), 2) or 3)")
            menu_two(teams, team_names)

        elif user_menu_selection2 == 1:
            display_stats(teams, team_names, 0)

        elif user_menu_selection2 == 2:
            display_stats(teams, team_names, 1)

        elif user_menu_selection2 == 3:
            display_stats(teams, team_names, 2)

    menu_one(teams, team_names)


def display_stats(teams, team_names, index):
    team = teams[index]
    team_name = team_names[index]

    team_stats_heading = """\n\nTeam: {} Stats
----------------------------"""
    total_number_players = "\nTotal players: {}"
    experienced_players = "\nexperienced players: {}"
    inexperienced_players = "\ninexperienced players: {}"
    names_of_players = "\nPlayers on Team:\n  {}"
    player_guardians = "\nGuardians:\n {}"

    average_height_display = "\nAverage Height: {}"
    continue_prompt = "\nEnter Any key + Enter to continue..."

    number_of_experienced_players = len([player for player in team if player['experience'] is True])
    number_of_inexperienced_players = len([player for player in team if player['experience'] is False])
    average_height = round(get_average_height(team))

    print(team_stats_heading.format(team_name))
    print(total_number_players.format(len(team)))
    print(experienced_players.format(number_of_experienced_players))
    print(inexperienced_players.format(number_of_inexperienced_players))

    # every players name in the team is put in one list and joined
    # by a ', ' then it is printed
    names = [name['name'] for name in team]
    print(names_of_players.format(", ".join(names)))

    # every the name of every players guardian is added to one list
    # and join by a ", " then it is printed
    guardians = []
    for player in team:
        for guardian in player['guardians']:
            guardians.append(guardian)

    print(player_guardians.format(", ".join(guardians)))

    # print the average height of the team
    print(average_height_display.format(average_height))

    # take an input from the user so that there can be delay between the last output
    # and the reprinting of menu one
    input(continue_prompt)
    menu_one(teams, team_names)


# Setting up the variables before the app runs
PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS


basket_ball_players = []
basket_ball_teams = []

if __name__ == "__main__":
    # clean the player date , make balance teams, and start the program.
    basket_ball_players = clean_player_data(PLAYERS)
    balanced_teams = make_balanced_teams(basket_ball_players)
    menu_one(balanced_teams, TEAMS)
