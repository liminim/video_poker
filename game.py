#! python3
# -*- coding: utf-8 -*-
#
# game.py
# Main game logic for video poker game


import cards



class Game():

    def __init__(self):

        self.cash = 100
        self.discard = []
        self.hand = [0, 0, 0, 0, 0]
        self.obj_deck = cards.Deck()
        self.deck = self.obj_deck.getDeck()


    def deal(self, num_cards=5):
        # Deal cards. Default set to 5 cards (full draw)
        draw = []
        for i in range(num_cards):
            draw.append(self.deck.pop(0))

        for i in draw:
            for index, card in enumerate(self.hand):
                if card == 0:
                    self.hand[index] = i
                    break
                

    def discardCards(self, cards):
        # Discard given list of cards and redraw them
        for card in cards:
            for index, value in enumerate(self.hand):
                if value == card:
                    self.discard.append(self.hand[index])
                    self.hand[index] = 0

        self.deal(len(cards))


    def checkCards(self):
        # Process current hand for a winner
        
        print(suit_count)
        for card in self.hand:
            pass
        

    def printHand(self):
        # Print console text version of current hand
        txt_hand = ''
        for i in self.hand:
            card_info = i.getInfo()
            txt_card = ''
            txt_card += card_info['name'] + card_info['u']
            txt_hand += txt_card + ' '

        return txt_hand



def test():
    # test function
    game = Game()
    game.deal()
    print(game.printHand())
    discarded = [game.hand[1], game.hand[3]]
    game.discardCards(discarded)
    print(game.printHand())
    game.checkCards()


if __name__ == '__main__':
    test()


    

        

        
            
            
            
