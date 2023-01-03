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

    #If the player moves first or not.
    def setFirstMove(self, isLast):
        if (isLast):
            self.firstMove = False
        else:
            self.firstMove = True

    #Set the character for player 1.
    def setPlayer(self, player):
        self.player = player

    #Switches character being drawn for the next move.
    def switchPlayer(self):
        if (self.player == 'X'):
            self.player = 'O'
        else:
            self.player = 'X'

    #Returns character of the current turn.
    def nextToMove(self):
        return self.player

    #Returns the character at the square (row, col).
    def get(self, row, col):
        return self.board(row, col)

    #Marks the square (row, col) with the character of the next player to move.
    def mark(self, row, col):

        #Cannot mark a non-empty square
        if (self.board.get(row, col) != '?'):
            return

        self.board.mark(row, col, self.player)

    #Marks the square (row, col) with value '?' (empty).
    def unmark(self, row, col):
        self.board.unmark(row, col)

    #Returns whether the game has terminated.
    def isOver(self):
        return self.board.winner() != '' or self.board.isFull()
    

    


    