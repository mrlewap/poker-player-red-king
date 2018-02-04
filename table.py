class Table:

    def countPeopeleInAllIn(self, game_state):
        player_in_all_in = 0

        for player in game_state['players']:
            if player["bet"] > 0 and player["stack"] == 0 and player["status"] != "out":
                player_in_all_in += 1

        return player_in_all_in

    def countPeopleInOut(self, game_state):
        player_in_all_out = 0

        for player in game_state['players']:
            if player["status"] == "out":
                player_in_all_out += 1

        return player_in_all_out

    def maxBet(self, game_state):
        player_index = game_state['in_action']
        id = game_state['players'][player_index]['id']
        max_bet = 0

        for player in game_state['players']:
            if player['id'] != id and player['bet'] > max_bet:
                max_bet = player['bet']

        return player_index

    def ourBet(self, game_state):
        player_index = game_state['in_action']
        return game_state['players'][player_index]['bet']

    def isBigBB(self, game_state):
        return (self.maxBet(game_state) - self.ourBet(game_state)) > self.maxBet(game_state) ** 2