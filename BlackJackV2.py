#!/usr/bin/env python3.8
import random
from random import shuffle
#Classes & Functions
# Ace is ranked 11 be default, will be able to drop in value elsewhere
cardRanks = {'Ace': 11,'Two': 2,'Three': 3,'Four': 4,'Five': 5,'Six': 6,'Seven': 7,'Eight': 8,'Nine': 9,'Ten': 10,'Jack': 10,'Queen': 10,'King': 10,}
cardSuits = ['Spades','Diamonds','Hearts','Clubs']
SuitSymbols = ['♠','♦','♥','♣']
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = self.cardRanks[rank]



class Table(object):
    def __init__(self,player):
        self.dealer = Dealer()
        self.player = Player(player)
        self.deck = Deck()

        self.table_setup()
    def table_setup(self):
        self.deck.shuffle()
        self.deal_card(self.player)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.dealer)
        self.count_score(self.player)
        self.count_score(self.dealer)
        self.main()

    def main(self):
        while True:
            print()
            print(self)
            player_move = self.player.hit_or_stick()
            if player_move:
                self.deal_card(self.player)
                self.count_score(self.player)
            else:
                self.dealer_hit()
        
    def dealer_hit(self):
        score = self.dealer.score
        while True:
            if score < 17:
                self.deal_card(self.dealer)
                self.count_score(self.dealer)
                print(self)
            else:
                self.check_final_score()

    def __str__(self):  # this is not just for checking progress during programming

        dealer_hand = [card for card, value in self.dealer.hand]
        player_hand = [card for card, value in self.player.hand]

        print("Dealer hand : {}".format(dealer_hand))
        print("Dealer score : {}".format(self.dealer.score))
        print()
        print("{}'s hand : {}".format(self.player.name, player_hand))
        print("{}'s score : {}".format(self.player.name, self.player.score))
        print("-" * 40)
        return ''



    def deal_card(self, player):
        card = self.deck.stack.pop()
        player.hand.append(card)
    def count_score(self, player):
        ace = False
        score = 0
        for card in player.hand:
            if card[1] == 1 and not ace:
                ace = True
                card = ('A', 11)
            score += card[1]
        player.score = score
        if player.score > 21 and ace:
            player.score -=10
            score = player.score
        self.win_check(score,player)
        return
    def win_check(self, score, player):
        if score > 21:
            print('{} Busted!'.format(player.name))
            self.gameover()
        elif score == 21:
            print('{} BlackJack!'.format(player.name))
            self.gameover()
        else:
            return
    def check_final_score(self):
        dealer_score = self.dealer.score
        player_score = self.player.score

        if dealer_score > player_score:
            print("The Dealer wins!")
            self.gameover()
        else:
            print("You win!")
            self.gameover()
    def gameover(self):
        if playagain():
            self.__init__(self.player.name)
            main()
        else:
            exit(1)

class Dealer(object):
    def __init__(self):
        self.name = "Dealer"
        self.score = 0
        self.hand = []

class Player(Dealer):

    def __init__(self,name):
        super().__init__()
        self.name = name


    @staticmethod
    def hit_or_stick():
        while True:
            choice = input("Will you take another card? ")
            if choice.lower().startswith('y'):
                return True
            elif choice.lower().startswith('n'):
                return False
            else:
                print("That isn't a valid input, enter yes or no to answer")
                continue

class Deck(object):
    def __init__(self):

        self.stack = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
                      ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
                      ('J', 10), ('Q', 10), ('K', 10)] * 4
        self.shuffle()
    def shuffle(self):
        shuffle(self.stack)
    def deal_card(self):
        card = self.stack.pop()
        return card

def playagain():
    print('Do you want to play another round?')
    return input().lower().startswith('y')
def main():
    print('''
 _     _            _    _            _    
| |   | |          | |  (♦)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                       _/ |  ♠  ♦  ♥  ♣       
                      |__/   By Finn Macrae   ''')
    player_name = input("Welcome to the casino!  What's your name? ")
    Table(player_name)

main()