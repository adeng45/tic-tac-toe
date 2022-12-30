from board import Board
import random

class AI:

    def __init__(self, level=0):
        self.level = level

    def randomSquare(self, board):

        empty = list(board.emptySquares())
        idx = random.randint(0, len(empty) - 1)

        return empty[idx]

    #Returns the value of the game without looking into future possibilities
    def staticEval(self, board, player):

        winner = board.winner()

        if (winner == player):
            return 1

        elif (winner != ''):
            return -1

        else:
           return 0


    # Returns favorability of the game, looks at the future search space
    def evalGame(self, game):

        #Could avoid this copying to save memory, but this is safer
        board = game.board.deepCopy()

        return self.evalBoard(board, True, game.nextToMove())

    
    # Helper function for evalGame, evaluates the board
    def evalBoard(self, board, isMax, player):

        value = self.staticEval(board, player)

        if (value == -1 or value == 1 or board.isFull()):
            return value

        bestCost = float('-inf') if isMax else float('inf')

        #Explore search space with backtracking
        for row, col in board.getEmptySquares():
            
            board.mark(row, col)

            cost = self.evalBoard(board, not isMax, player)

            # Backtrack
            board.unmark(row, col)

            if (isMax):

                if (cost > bestCost):
                    bestCost = cost
            
            else:
                
                if (cost < bestCost):
                    bestCost = cost

        return bestCost


    #Find best move
    def bestMove(self, game):

        #Could avoid copying to save memory, but this is safer
        board = game.board.deepCopy()

        player = game.nextToMove()
        bestCost = float('-inf')
        bestMove = None

        #Iterate through possible moves
        for row, col in board.getEmptySquares():

            board.mark(row, col)

            cost = self.evalBoard(board, False, player)

            board.unmark(row, col)

            if (cost > bestCost):
                bestCost = cost
                bestMove = (row, col)

        return bestMove
    

    # All-in-one
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


                











        



