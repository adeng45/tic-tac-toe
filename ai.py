from board import Board
import random

class AI:

    def __init__(self, level=0):
        self.level = level

    def randomSquare(self, board):

        empty = list(board.emptySquares())
        idx = random.randint(0, len(empty) - 1)

        return empty[idx]

    #Handles comparison between two values dependent on min/max objective
    def comp(self, cost, currCost, isMax):
        
        if (isMax):
            return cost > currCost

        else:
            return cost < currCost


    def playerSwitch(self, player):
        if (player == 'X'):
            return 'O'

        else:
            return 'X'

    #Returns the value of the game without looking into future possibilities
    def staticEval(self, board):

        winner = board.winner()

        if (winner == 'X'):
            return 1

        elif (winner != ''):
            return -1

        else:
           return 0


    # Helper function for evalGame, evaluates the board
    def evalBoard(self, board, isMax, player):

        value = self.staticEval(board)

        if (value == -1 or value == 1 or board.isFull()):
            return value

        bestCost = float('-inf') if isMax else float('inf')

        #Explore search space with backtracking
        for row, col in board.getEmptySquares():
            
            board.mark(row, col, player)

            cost = self.evalBoard(board, not isMax, self.playerSwitch(player))

            board.unmark(row, col)

            if (self.comp(cost, bestCost, isMax)):
                bestCost = cost

        return bestCost


    #Find best move
    def bestMove(self, game):

        #Could mutate the board directly, but this is safer/cleaner
        board = game.board.deepCopy()

        player = game.nextToMove()
        isMax = True if player == 'X' else False
        bestCost = float('-inf') if isMax else float('inf')
        bestMove = None

        #Iterate through possible moves
        for row, col in board.getEmptySquares():

            board.mark(row, col, player)

            cost = self.evalBoard(board, isMax, self.playerSwitch(player))

            board.unmark(row, col)

            if (self.comp(cost, bestCost, isMax)):
                bestCost = cost
                bestMove = (row, col)

        return bestMove
    

    # All-in-one, calculates cost while finding the best move. Mutates the board!
    # def findMove(self, game):
        
    #     board = game.board

    #     #Random choice
    #     if (self.level == 0):
    #         return self.randomSquare(self, board)

    #     #Minimax 
    #     elif (self.level == 1):

    #         bestMoveCost = float('-inf') if game.toMove() == 'X' else float('inf')
    #         bestMove = None

    #         #Explore search space with backtracking
    #         for row, col in board.getEmptySquares():
                
    #             game.mark(row, col)

    #             #Check if game is over
    #             if (game.isOver()):
                    
    #                 cost = self.staticEval(board, 'X')

    #             #Recurse onwards                
    #             else:
    #                 cost, move = self.findMove(game)

    #             move = (row, col)

    #             #Backtrack
    #             game.unmark(row, col)

    #             if (game.toMove() == 'X'):

    #                 if (cost > bestMoveCost):
    #                     bestMoveCost = cost
    #                     bestMove = move
                
    #             else:
                    
    #                 if (cost < bestMoveCost):
    #                     bestMoveCost = cost
    #                     bestMove = move

    #         return bestMoveCost, bestMove


                











        



