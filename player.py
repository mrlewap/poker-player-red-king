from hand import Hand

class Player:
    VERSION = "Red King 0.2"

    def betRequest(self, game_state):
         player_index = game_state['in_action']

         hand = Hand()
         hand.setHand(game_state['players'][player_index]['hole_cards'])

         return hand.resolveStrategy(game_state)

    def showdown(self, game_state):
        pass

