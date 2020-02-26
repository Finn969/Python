#!/usr/bin/env python3.8

game = True

while game:
    player_session = input("Do you wantg to continue (y/n): ")

    if player_session.lower() == "n":
        game = False
    elif player_session.lower() == "y":
        pass
    else:
        print('Please enter a valid input: [y]es or [n]o')