#!#!/usr/bin/env python3.8
#any imports

team = ['white', 'black']
#classes
class Chess_piece():
    def __init__(self,name,team,distance,icon,position):
        self.name = name
        self.team = team
        self.distance = distance
        self.position = position

class Pawn(Chess_piece):
    distance = 1
    if team == 'white':
        icon = '♟'
    else:
        icon = '♙'

class Knight(Chess_piece):
    distance = 2
    if team == 'white':
        icon = '♞'
    else:
        icon = '♘'

class Bishop(Chess_piece):
    distance = 8
    if team == 'white':
        icon = '♝'
    else:
        icon = '♗'

class Rook(Chess_piece):
    distance = 8
    if team == 'white':
        icon = '♜'
    else:
        icon = '♖'

class Queen(Chess_piece):
    distance = 8
    if team == 'white':
        icon = '♛'
    else:
        icon = '♕'

class King(Chess_piece):
    distance = 1
    if team == 'white':
        icon = '♚'
    else:
        icon = '♔'











def title():
    print('''      _                                              _:_
     | |  By Finn Macrae                            '-.-'
  ___| |__   ___  ___ ___                  ()      __.'.__
 / __| '_ \ / _ \/ __/ __|              .-:--:-.  |_______|
| (__| | | |  __/\__ \__ \       ()      \____/    \=====/
 \___|_| |_|\___||___/___/       /\      {====}     )___(
                      (\=,      //\\\\      )__(     /_____\  
      __    |'-'-'|  //  .\    (    )    /____\     |   |
     /  \   |_____| (( \_  \    )__(      |  |      |   |
     \__/    |===|   ))  `\_)  /____\     |  |      |   |
    /____\   |   |  (/     \    |  |      |  |      |   |
     |  |    |   |   | _.-'|    |  |      |  |      |   |
     |__|    )___(    )___(    /____\    /____\    /_____\  
    (====)  (=====)  (=====)  (======)  (======)  (=======)
    }===={  }====={  }====={  }======{  }======{  }======={
   (______)(_______)(_______)(________)(________)(_________))''')

    print('\n' * 2)
    print('Welcome! ')










def print_chessboard():
    print(" ")
    for i in range('a'-'h'):# column headers
        print( " " + str(i) + " ")
    print("\n")

    for i in range(7):# row headers
        if i != 6:
            print (str(i+1)+ "  ")
        else:
            print (str(i+1) + " ")
        
        for j in range('a'-'h'):




title()