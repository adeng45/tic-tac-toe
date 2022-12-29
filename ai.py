from board import Board
import random

class AI:

    def __init__(self, level=0):
        self.level = level

    def randomSquare(self, board):

        empty = list(board.emptySquares())
        idx = random.randint(0, len(empty) - 1)

        return empty[idx]



    def findMove(self, game):
        
        board = game.board

        #Random choice
        if (self.level == 0):
            return self.randomSquare(self, board)

        #Minimax 
        elif (self.level == 1):

            totalCost = 0 
            bestMoveCost = float('-inf') if game.toMove == 'X' else float('inf')
            bestMove = None

            #Explore search space with backtracking
            for row, col in board.getEmptySquares():
                
                game.mark(row, col)
                # print(row, col)

                #Check if game is over
                if (game.isOver()):
                    
                    winner = game.board.winner()

                    if (winner == 'X'):
                        cost = 1

                    elif (winner == 'O'):
                        cost = -1

                    else:
                        cost = 0

                    move = (row, col)

                #Recurse onwards                
                else:
                    cost, move = self.findMove(game)

                game.unmark(row, col)

                totalCost += cost

                if (game.toMove == 'X'):

                    if (bestMoveCost < cost):
                        bestMoveCost = cost
                        bestMove = move
                
                else:
                    if (bestMoveCost > cost):
                        bestMoveCost = cost
                        bestMove = move

            return totalCost, bestMove


                











        



