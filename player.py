
class Player:
    VERSION = "Red King"

    def betRequest(self, game_state):
        return game_state['players'][game_state['in_action']]['stack']

    def showdown(self, game_state):
        pass

