
class Table:

    def countPeopleInAllIn(self, game_state):
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

    def countPeopleInActive(self, game_state):
        player_in_all_active = 0

        for player in game_state['players']:
            if player["status"] == "active":
                player_in_all_active += 1

        return player_in_all_active

    def notOurMaxBet(self, game_state):
        player_index = game_state['in_action']
        id = game_state['players'][player_index]['id']
        max_bet = 0

        for player in game_state['players']:
            if player['id'] != id and player['bet'] > max_bet:
                max_bet = player['bet']

        return max_bet

    def ourBet(self, game_state):
        player_index = game_state['in_action']
        return game_state['players'][player_index]['bet']

    def isBigBB(self, game_state):
        return (self.notOurMaxBet(game_state) - self.ourBet(game_state)) > game_state['small_blind'] * 2

    def getCurrentRound(self, game_state):
        return game_state['round']

