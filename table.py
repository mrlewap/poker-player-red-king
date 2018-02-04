class Table:

    def countPeopeleInAllIn(self, game_state):
        player_in_all_in = 0

        for player in game_state['players']:
            if player["bet"] == player["stack"]:
                player_in_all_in += 1

        return player_in_all_in