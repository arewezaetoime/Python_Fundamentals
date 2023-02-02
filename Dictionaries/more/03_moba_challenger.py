def print_results():
    for player in pool_players.keys():
        print(f"{player}: {sum(pool_players[player].values())} skill")
        for position, skill in pool_players[player].items():
            print(f'- {position} <::> {skill}')


def check_positions(player1, player2):
    for current_position in pool_players[player1].keys():
        if current_position in pool_players[player2].keys():
            return True, current_position
    return False


def duel(player1, player2, position_found):
    if player1 in pool_players.keys() and player2 in pool_players.keys():
        if check_positions(player1, player2):
            # Position both players play
            position_found = check_positions(player1, player2)[1]
            if pool_players[player1][position_found] > pool_players[player2][position_found]:
                del pool_players[player2]
            else:
                del pool_players[player1]
            # if pool_players[player1][position_found] == pool_players[player2][position_found]:


def add_players_to_pool(player, position, skill):
    # Here we add players to the pool.
    if player not in pool_players.keys():
        pool_players[player] = {position: int(skill)}
    else:
        if position in pool_players[player] and int(skill) > pool_players[player][position]:
            pool_players[player][position] = int(skill)
        elif position not in pool_players[player]:
            pool_players[player].update({position: int(skill)})


def get_players():
    # Here we get players and determine what to do with the data. We either send them to the add_players function to
    # add/update the dict with the info given or we send them to the duel function.
    command = input()
    while command != 'Season end':
        if '->' in command:
            player, position, skill = command.split(' -> ')
            add_players_to_pool(player, position, skill)

        elif 'vs' in command:
            player_one, player_two = command.split(' vs ')
            position_found = ''
            duel(player_one, player_two, position_found)

        command = input()


pool_players = {}
get_players()
print_results()