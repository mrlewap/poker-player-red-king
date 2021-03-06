from hand import Hand

class Player:
    VERSION = "children card game"

    def betRequest(self, game_state):
        try:
         player_index = game_state['in_action']

         hand = Hand()
         hand.setHand(game_state['players'][player_index]['hole_cards'])

         return hand.resolveStrategy(game_state, player_index)
        except BaseException as ex:
            print(ex)
            return game_state['players'][game_state['in_action']]['stack']

    def showdown(self, game_state):
        pass

