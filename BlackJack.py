#!/usr/bin/env python3

import random
Rank = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King' }
Suit = { 'c': 'Clubs', 'h': 'Hearts', 's': 'Spades', 'd': 'Diamonds' }

card = [Rank, Suit]
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def CardName(self):
        return " of ".join((self.rank, self.suit))
    def getRank(self):
        return(self.rank)
    def getSuit(self):
        return(self.suit)

def BJscore(Card):
    if Card.rank > 9: #Face cards each worth 10
            return(10)
    if Card.rank == 1: #Aces can switch between 11 and 1
        if totalScore > 21:
            return(1)

        else:
            return(11)

class Deck:
    def __init__(self):
        self.cards = [Card(r,s) for r in[Rank] for s in [Suit]]
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    def deal(self):
        if len(self.cards)>1:
            return self.cards.pop(0)

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)



def endgame(count):
    print("BlackJack! I will come up with how to write results here")

def showHand(Hand):
    for card in hand:
        print

#Title screen
print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                       _/ |                
                      |__/   By Finn Macrae   ''')

gameover = False

while gameover == False:
    # Play the game