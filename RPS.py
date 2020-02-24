
from random import randint
c = ["Rock", "Paper", "Scissors"]

AI = c[randint(0,2)]

player = False
wins = 0
losses = 0
ties = 0

rocks = 0
papers = 0
scissors = 0
while player == False:
    print("You have won",wins,"times.")
    print("You have lost",losses,"times.")
    print("You have tied",ties,"times.")
    print("")
    
    player = input("Rock, Paper, Scissors! ")
    print ("")
    if player == AI:
        print("It's a tie! Try again!")
        ties = ties + 1
    elif player == "Rock":
        if AI == "Paper":
            print("You lose!", AI, "covers", player)
            losses = losses + 1
        else:
            print("You win!", player, "smashes", AI)
            wins = wins + 1
    elif player == "Paper":
        if AI == "Scissors":
            print("You lose!", AI, "cut", player)
            losses = losses + 1
        else:
            print("You win!", player, "covers", AI)
            wins = wins + 1
    elif player == "Scissors":
        if AI == "Rock":
            print("You lose!", AI, "smashes", player)
            losses = losses + 1
        else:
            print("You win!", player, "cut", AI)
            wins = wins + 1
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    AI = c[randint(0,2)]