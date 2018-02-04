from card import Card

class Hand:
    def __init__(self):
        self.cards_in_hand = []
        pass

    def setHand(self, hand):
        for each in hand:
            card = Card(each.rank, each.suit)
            self.cards_in_hand.append(card)

    def resolveStrategy(self, game_state):
        if self.resolveValue(self.cards_in_hand[0].rank) == self.resolveValue(self.cards_in_hand[1].rank):
            return game_state['players'][game_state['in_action']]['stack']

        if self.resolveValue(self.cards_in_hand[0].rank) >= 10 and self.resolveValue(self.cards_in_hand[1].rank) >= 10:
            return game_state['players'][game_state['in_action']]['stack']

        return 0


    def resolveValue(self, value):
        if value == 'J' or value == 'j':
            return 11
        elif value == 'Q' or value == 'q':
            return 12
        elif value == 'K' or value == 'k':
            return 13
        elif value == 'A' or value == 'a':
            return 14
        else:
            return int(value)