#https://youtu.be/t8YkjDH86Y4

import random

class Cards(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            for v in range(1,14):
                self.cards.append(Cards(s,v)) #Adding all cards in the Cards Class
                # print("{} of {}".format(v, s))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0 , -1): #backwards
            r = random.randint(0,i) # 0 to high value of i
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self): # to randomly draw a card to pickup by a player (in the player class)
        return self.cards.pop()


class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self, deck): # A player can draw a card from any deck
        self.hand.append(deck.drawCard())  #Appending cards in a player hand from drawn cards
        return self

    def showHand(self): # to show all cards those are in a player's hand
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


card = Cards("Clubs", 6)
card.show()
print(card.suit)
#===========
# print("==All Decks===")
# deck = Deck()
# deck.show()
#
# print()
# print("==After Shuffle ===")
# deck.shuffle()
# deck.show()
#
# print()
# print("==After building cards ===")
# deck.build()
# deck.show()
#
# print()
# print("==After popping ===")
# card = deck.drawCard()
# card.show()
#
# #=========
#
# rafi = Player("Rafi")
# rafi.draw(deck).draw(deck) #draw(deck) for each card. Here, two cards will be drawn.
# rafi.showHand()
#
# print("==Removing card===")
#
# dis = rafi.discard()
# rafi.showHand()