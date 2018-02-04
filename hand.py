from card import Card
from table import Table

class Hand:
    def __init__(self):
        self.cards_in_hand = []

    def setHand(self, hand):
        for each in hand:
            card = Card(each['rank'], each['suit'])
            self.cards_in_hand.append(card)

    def resolveStrategy(self, game_state, player_index):
        table = Table()
        if table.countPeopleInOut(game_state) == 3:
            if self.redZoneForThreePeople(game_state):
                return game_state['players'][game_state['in_action']]['stack']
            else:
                return 0

        if table.countPeopleInActive(game_state) == 1:
            current_max = game_state['current_buy_in']
            if (current_max - table.ourBet(game_state)) <= game_state['small_blind'] * 2:
                return game_state['current_buy_in'] - game_state['players'][player_index]['bet']

        if self.betGreaterThanBB(game_state):
            if self.isInRedZone(game_state):
                return game_state['players'][game_state['in_action']]['stack']
            else:
                if table.searchActivePlayerByName(game_state, 'PolniyDom'):
                    if self.isInOrangeZone(game_state):
                        return game_state['players'][game_state['in_action']]['stack']
                    else:
                        return 0
                else:
                    return 0
        else:
            if self.notOurBetIsGreaterThanBB(game_state):
                if self.isInRedZone(game_state):
                    return game_state['players'][game_state['in_action']]['stack']
                else:
                    return 0
            else:
                if self.slagCards():
                    return 0
                else:
                    return \
                    game_state['current_buy_in'] - game_state['players'][player_index]['bet'] + game_state['minimum_raise']

    def notOurBetIsGreaterThanBB(self, game_state):
        if game_state['current_buy_in'] > (game_state['small_blind'] * 2):
            return True
        return False

    def isInRedZone(self, game_state):
        if self.resolveValue(self.cards_in_hand[0].card_value) == self.resolveValue(self.cards_in_hand[1].card_value) and \
            self.cards_in_hand[0].card_value >= 9:
            return True
        if self.resolveValue(self.cards_in_hand[0].card_value) >= 11 and \
                self.resolveValue(self.cards_in_hand[1].card_value) >= 11 and \
                self.isPairSute():
            return True

        return False

    def redZoneForThreePeople(self, game_state):
        if (self.resolveValue(self.cards_in_hand[0].card_value) == self.resolveValue(self.cards_in_hand[1].card_value)) \
                and self.cards_in_hand[0].card_value >= 12:
            return True
        return False


    def isInOrangeZone(self, game_state):
        if self.resolveValue(self.cards_in_hand[0].card_value) == self.resolveValue(self.cards_in_hand[1].card_value):
            return True

        if self.resolveValue(self.cards_in_hand[0].card_value) >= 9 and self.resolveValue(self.cards_in_hand[1].card_value) >= 9:
            return True

        return False

    def betGreaterThanBB(self, game_state):
        if game_state['current_buy_in'] > (game_state['small_blind'] * 2):
            return True
        return False

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

    def isPairSute(self):
        return self.cards_in_hand[0].card_suit == self.cards_in_hand[1].card_suit

    def slagCards(self):
        if ((self.resolveValue(self.cards_in_hand[0].card_value) <= 6) and (self.resolveValue(self.cards_in_hand[1].card_value) <= 9))\
                or ((self.resolveValue(self.cards_in_hand[1].card_value) <= 6) and (self.resolveValue(self.cards_in_hand[0].card_value) <= 9))\
                and not (self.resolveValue(self.cards_in_hand[0].card_value) == self.resolveValue(self.cards_in_hand[1].card_value)):
            return True
        else:
            return False

