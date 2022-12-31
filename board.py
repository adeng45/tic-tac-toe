import numpy as np
from constants import *

class Board:

    def __init__(self):
        self.arr = np.full( (ROWS, COLS) , '?')
        self.emptySquares = set()
        for row in range(ROWS):
            for col in range(COLS):
                self.emptySquares.add( (row, col) )
        
    
    def deepCopy(self):

        board = Board()

        for row, col, player in self.fetch():
            if (player != '?'):
                board.mark(row, col, player)

        return board

    def isSquareEmpty(self, row, col):
        return (row, col) in self.emptySquares

    def getEmptySquares(self):
        return self.emptySquares

    def isFull(self):
        return len(self.emptySquares) == 0

    def unmark(self, row, col):
        self.arr[row][col] = '?'
        self.emptySquares.add( (row, col) )


    def mark(self, row, col, player):
        self.arr[row][col] = player
        self.emptySquares.remove( (row, col) )

    def clear(self):
        self.arr = np.full( (ROWS, COLS) , '?')

    def show(self):

        for row in range(ROWS):
            
            print('[', end='')
            
            for col in range(COLS):
                print(self.arr[row][col], end='')
                if (col != COLS - 1):
                    print(', ', end='')

            print(']')

    def get(self, row, col):
        return self.arr[row][col]

    def fetch(self):

        for row in range(ROWS):
            for col in range(COLS):
                yield (row, col, self.get(row, col))

    def winner(self):

        #Horizontal wins
        for row in range(ROWS):
            for col in range(1, COLS):
                if (self.get(row, col) != self.get(row, col - 1)):
                    break
                if (col == COLS - 1 and self.get(row, col) != '?'):
                    return self.get(row, col)

        #Vertical wins
        for col in range(COLS):
            for row in range(1, ROWS):
                if (self.get(row, col) != self.get(row - 1, col)):
                    break
                if (row == ROWS - 1 and self.get(row, col) != '?'):
                    return self.get(row, col)

        #Top-left to bottom-right diagonal
        for i in range(1, ROWS):
            if (self.get(i, i) != self.get(i - 1, i - 1)):
                break
            if (i == ROWS - 1 and self.get(i, i) != '?'):
                return self.get(i, i)


        #Top-right to bottom-left diagonal
        for i in range(1, ROWS):
            if (self.get(i, ROWS - 1 - i) != self.get(i - 1, (ROWS - 1 - i) + 1)):
                break
            if (i == ROWS - 1 and self.get(i, ROWS - 1 - i) != '?'):
                return self.get(i, ROWS - 1 - i)

        return ''

                
# Board().show()



