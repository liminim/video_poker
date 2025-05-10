#! python3
# -*- utf-8 -*-
#
# cards.py
# classes for a full standard deck of playing cards


import random


C_VALUES = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}

C_SUITS = {
    'Hearts': u'\u2665',
    'Diamonds': u'\u2666',
    'Clubs': u'\u2663',
    'Spades': u'\u2660'
}

def  _other_cmp_filter(obj):
        if type(obj) is Deck:
            len_other = len(obj.deck['deck'])
        else:
            len_other = len(obj)

        return len_other

class Card():

    def __init__(self, val, name, suit, symb):
        # initialize individual card
        self.value = val
        self.name = str(name)
        self.suit = suit
        self.symb = symb

    def __cmp__(self, other):
        
        if other is not Card:
            return False
        return self.value == other.value
    
    def __gt__(self, other):
        if other is not Card:
            return False
        return self.value > other.value
    
    def __lt__(self, other):
        if other is not Card:
            return False
        return self.value < other.value
    
    def __ge__(self, other):
        if other is not Card:
            return False
        return self.value >= other.value
    
    def __le__(self, other):
        if other is not Card:
            return False
        return self.value <= other.value
    
    def __str__(self):
        return f'{self.name}{self.symb}'
    
    def __int__(self):
        return self.value

    def info(self):
       # Return info on card instance
        return {'name': self.name, 'suit': self.suit, 'value': self.value,
                'u': self.symb}
        

class Deck():

    def __init__(self):
        # initialize deck object
        self.deck_groups = ['deck', 'discard', 'hand']
        self.new_deck
    
    def __int__(self):
        return len(self.deck['deck'])

    def __str__(self):
        return self.print_deck()
 
    def __gt__(self, other):
        len_other = _other_cmp_filter(other)
        len_self = int(self)
        return len_self > len_other
    
    def __lt__(self, other):
        len_other = _other_cmp_filter(other)
        len_self = len(self.deck['deck'])
        return len_self < len_other
    

    def __eq__(self, other):
        len_other = _other_cmp_filter(other)
        len_self = len(self.deck['deck'])

        return len_self == len_other

    def new_deck(self):        
        # Build new list of card objects based on decriptor globals
        self.deck = {'deck':[], 
                     'discard':[], 
                     'hand':[],
                     'board':[]
                    }
        for suit, symb in C_SUITS.items():
            for key, value in C_VALUES.items():
                self.deck['deck'].append(Card(value, key, suit, symb))           

    def shuffle_deck(self):        
        # Shuffle deck list
        if len(self.deck['deck']) > 0:
            random.shuffle(self.deck['deck'])
        
        else:
            return print("ERROR - NO DECK HAS BEEN BUILT")
    
    def draw(self, qty=0, top=True, hand=True):
        if top:
            drawn = self.deck['deck'].pop(0)    # Draw top of deck
        else:
            drawn = self.deck['deck'].pop(-1)   # Draw bottom of deck
        
        if hand:
            self.deck['hand'].append(drawn)     # Put drawn card in hand
        else:
            self.deck['discard'].append(drawn)  # Put drawn card in discard
        return drawn


    def print_deck(self, opt='deck'):
        opt = opt.lower().strip()
        if opt not in self.deck_groups:
            print(
f"""\nInvalid call to [opt].
Use '{self.deck_groups[0]}', '{self.deck_groups[1]}' or '{self.deck_groups[2]}'
""")
            return '{EMPTY}'
        cards = ''
        for card in self.deck['deck']:
            cards += (str(card) + ' ')
        return cards


def _test_print(title, deck):
    print(f'\n{title}\n{'~' * len(title)}\n{str(deck)}')


if __name__ == '__main__':
    deck_test = Deck()
    print()
    deck_test.new_deck()
    _test_print('New Deck', deck_test)
    deck_test.shuffle_deck()
    _test_print('Shuffle 1', deck_test)
    deck_test.shuffle_deck()
    _test_print('Shuffle 2', deck_test)
    draw_one = deck_test.draw()
    _test_print('1st Draw', draw_one)
    draw_two = deck_test.draw()
    _test_print('2nd Draw', draw_two)
    draw_three = deck_test.draw()
    _test_print('3rd Draw', draw_three)
    draw_bottom = deck_test.draw(top=False)
    _test_print('Draw from bottom', draw_bottom)
    handstring = ''
    for card in deck_test.deck['hand']:
        handstring += str(card) + ' '
    _test_print('Current Hand', handstring)

    _test_print(f'Remaining cards in deck ({int(deck_test)})', deck_test)

#    deck_test.print_deck(opt='bad_call')
