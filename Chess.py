#!#!/usr/bin/env python3.8
#any imports
White = {'name': "White"}
Black = {'name': "Black"}
Columns = list('abcdefgh')
Rows = [int(x) for x in str(12345678)]
Chessboard = [Columns,Rows]

#imported from drawchess. Hopefully will get a nice looking board





def geticon(i):
    if White:
        icon = ''.join(chr(9812+i))
    else:
        icon = ''.join(chr(9812-i))

#classes
class Game(object):
    def printboard(self):

        topbottom=['*','a','b','c','d','e','f','g','h','*']
        sides=['1','2','3','4','5','6','7','8']
        tbspacer=' '*6
        rowspacer=' '*5
        cellspacer=' '*4
        empty=' '*3
        print
        for field in topbottom:
            print ("%4s" % field)
        print
        print (tbspacer+("_"*4+' ')*8)
        for row in range(8):
            print(rowspacer+(('|'+cellspacer)*9))
            print ("%4s" % sides[row],('|'))
            for col in range(8):
                if (row, col) not in self.board:
                    print (empty+'|')
                else:
                    print ("%2s" % self.board[(row, col)],('|'))
            print ("%2s" % sides[row])
            print
            print (rowspacer+'|'+(("_"*4+'|')*8))
        print
        for field in topbottom:
            print ("%4s" % field)
        print ("\n")



class Team():
    def __init__(self, colour):
        self.colour = colour



class Chess_piece():
    def __init__(self,name,team,distance,position,rank):
        self.name = name
        self.team = White,Black
        self.distance = distance
        self.position = position
        self.rank = rank

class Pawn(Chess_piece):
    def __init__(self, name='pawn', team, distance=1, rank=1, icon=geticon(rank)):
        super().__init__(name, team, distance, position, rank)

class Knight(Chess_piece):
    def __init__(self, name='pawn', team, distance=1, rank=2, icon=geticon(rank)):
    distance = 2
    if team == 'white':
        icon = '♞'
    else:
        icon = '♘'

class Bishop(Chess_piece):
    def __init__(self, name='pawn', team, distance=1, rank=3, icon=geticon(rank)):
    distance = 8
    if team == 'white':
        icon = '♝'
    else:
        icon = '♗'

class Rook(Chess_piece):
    def __init__(self, name='pawn', team, distance=8, rank=4, icon=geticon(rank)):
    distance = 8
    if team == 'white':
        icon = '♜'
    else:
        icon = '♖'

class Queen(Chess_piece):
    def __init__(self, name='pawn', team, distance=8, rank=5, icon=geticon(rank)):
    distance = 8
    if team == 'white':
        icon = '♛'
    else:
        icon = '♕'

class King(Chess_piece):
    def __init__(self, name='king', team, distance=1, rank=6, icon=geticon(rank)):












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







title()
game = Game():
    printboard(game)