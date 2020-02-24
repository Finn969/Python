from random import randint
c = ["r", "p", "s"]

player = False

rocks = 0
papers = 0
scissors = 0

wins = 0
losses = 0
ties = 0

computer = c[randint(0,2)]
       

while player == False:
    player = input("[r]ock, [p]aper, [s]cissors! ")
    print("")
    if player == "r":
        rocks = rocks + 1
        if computer == "r":
            print(player, "versus", computer,"!")
            print("It's a tie! Try again!")
            ties = ties + 1

        elif computer == "p":
            print(player, "versus", computer,"!")
            print("You lose! Paper covers rock!")
            losses = losses + 1

        else:
            print(player, "versus", computer,"!")
            print("You win! Rock smashes scissors!")
            wins = wins + 1

    elif player == "p":
        papers = papers + 1
        if computer == "r":
            print(player, "versus", computer,"!")
            print("You win! Paper covers rock!")
            wins = wins + 1

        elif computer == "p":
            print(player, "versus", computer,"!")
            print("It's a tie! Try again!")
            ties = ties + 1

        else:
            print(player, "versus", computer,"!")
            print("You lose! Scissors cut paper!")
            losses = losses + 1

    elif player == "s":
        scissors = scissors + 1
        if computer == "r":
            print(player, "versus", computer,"!")
            print("You lose! Rock smashes scissors!")
            losses = losses + 1

        elif computer == "p":
            print(player, "versus", computer,"!")
            print("You win! Scissors cut paper!")
            wins = wins + 1

        else:
            print(player, "versus", computer,"!")
            print("It's a tie! Try again!")
            ties = ties + 1

    else:
        print("That doesn't look valid; type 'r', 'p' or 's' to select!")

    if rocks>papers and rocks>scissors:
        computer == c[1]
        
    elif papers>rocks and papers>scissors:
        computer == c[2]
        
    elif scissors>rocks and scissors>papers:
        computer == c[0]
        
    else:
        computer = c[randint(0,2)]

    player = False
