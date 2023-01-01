from board import Board
from constants import * 

class Game:
    
    def __init__(self):
        self.ai = False
        self.autoplay = False
        self.player = 'X'
        self.firstMove = True
        self.board = Board()
        self.exists = False

    def setFirstMove(self, isLast):
        if (isLast):
            self.firstMove = False
        else:
            self.firstMove = True

    def exists(self):
        return self.exists

    def nextToMove(self):
        return self.player

    def get(self, row, col):
        return self.board(row, col)

    def mark(self, row, col):

        #Cannot mark a non-empty square
        if (self.board.get(row, col) != '?'):
            return

        self.board.mark(row, col, self.player)

    def unmark(self, row, col):
        self.board.unmark(row, col)

    def switchPlayer(self):
        if (self.player == 'X'):
            self.player = 'O'
        else:
            self.player = 'X'

    def isOver(self):
        return self.board.winner() != '' or self.board.isFull()
    

    


    