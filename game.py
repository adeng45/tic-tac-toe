from board import Board
from constants import * 

class Game:
    
    def __init__(self):
        self.ai = False
        self.player = 'X'
        self.board = Board()
        pass


    def toMove(self):
        return self.player

    def get(self, row, col):
        return self.board(row, col)

    def mark(self, row, col):

        #Cannot mark a non-empty square
        if (self.board.get(row, col) != '?'):
            return

        self.board.mark(row, col, self.player)
        self.switchPlayer()
        # self.board.show()

    def unmark(self, row, col):
        self.board.unmark(row, col)
        self.switchPlayer()

    def switchPlayer(self):
        if (self.player == 'X'):
            self.player = 'O'
        else:
            self.player = 'X'

    def isOver(self):
        return self.board.winner() != '' or self.board.isFull()
    

    


    