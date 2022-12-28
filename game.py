from board import Board
from constants import * 

class Game:
    
    def __init__(self):
        self.history = []
        self.AI = False
        self.player = 'X'
        self.board = Board()
        pass

    def get(self, row, col):
        return self.board(row, col)

    def mark(self, row, col):

        #Cannot mark a non-empty square
        if (self.board.get(row, col) != '?'):
            return

        self.board.mark(row, col, self.player)
        self.switchPlayer()
        self.history.append( (row, col) )
        # self.board.show()

    def switchPlayer(self):
        if (self.player == 'X'):
            self.player = 'O'
        else:
            self.player = 'X'

    


    