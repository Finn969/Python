#!/usr/bin/env python3.8
#imports
from random import randint
import os
#classes
class Ship:
    def __init__(self, size, orientation, location)
    self.size = size
    self.orientation = orientation

    if orientation == 'h':
        self.coordinates = []
        for index in range(size):
            self.coordinates.append({'row': location['row'], 'col': location['col'] + index})
    else:
        self.coordinates = []
        for index in range(size):
            self.coordinates.append({'row': location['row'] + index, 'col': location['col']})
    def filled(self):
        for coords in self.coordinates:
            if board[coords['row']][coords['col']] == 1:
            return True
        return False
  
    def fillBoard(self):
        for coords in self.coordinates:
            board[coords['row']][coords['col']] = 1

    def contains(self, location):
        for coords in self.coordinates:
            if coords == location:
                return True
            return False
  
    def destroyed(self):
        for coords in self.coordinates:
            if board_display[coords['row']][coords['col']] == 'O':
                return False
            elif board_display[coords['row']][coords['col']] == '*':
                raise RuntimeError("Board display inaccurate")
        return True
#settings
row_size = 9
col_size = 9
num_ships = 4
max_ship_size = 5
min_ship_size = 2
num_turns = 40
#lists
ship_list = []

board = [[0] * col_size for x in range(row_size)]

board_display = [["O"] * col_size for x in range(row_size)]

def print_board(board_array):
  print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
  for r in range(row_size):
    print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
  print()