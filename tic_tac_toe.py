import sys
import pygame
from pygame import gfxdraw

from game import Game
from ai import AI
from constants import * 

#Initialization 
def init():
    pygame.init()
    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption('<Tic-Tac-Toe>')

def colorBoard(screen, color):
    screen.fill(BOARD_COLOR)

def drawLines():

    #Horizontal
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

    #Vertical
    for j in range(1, COLS):
        pygame.draw.line(screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def drawBoard(game):
    
    for row, col, player in game.board.fetch():

        # X
        if (player == 'X'):
            topLeft = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + OFFSET)
            bottomRight = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, topLeft, bottomRight, CROSS_WIDTH)

            bottomLeft = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            topRight = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, bottomLeft, topRight, CROSS_WIDTH)

        # O
        elif (player == 'O'):
            center = ( col * SQUARE_SIZE + SQUARE_SIZE / 2 , row * SQUARE_SIZE + SQUARE_SIZE / 2 )
            pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

        # None
        else:
            continue
    
def vspace():
    print()
    print()

def terminalEngine(game):

    game.start()

    while (not game.isOver()):

        game.board.show()
        print('Your move!')

        squareNumber = None

        while ( not (isinstance(squareNumber, str) and len(squareNumber) > 0 and 1 <= int(squareNumber) <= 9) ):

            if (squareNumber != None):
                vspace()
                print('Invalid square number, try again!')

            squareNumber = input()


        row = (int(squareNumber) - 1) // COLS
        col = (int(squareNumber) - 1) % COLS

        #Square is already played
        if (not game.board.isSquareEmpty(row, col)):
            vspace()
            print('That square is already taken, try again!')
            vspace()
            continue
            
        game.mark(row, col)
        game.switchPlayer()
        vspace()

    
    game.board.show()
    game.finish()
    print('Player {0} wins!'.format(game.board.winner()))

def GUIEngine(game):

    for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                pygame.quit()
                cont = False
                break

            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos = event.pos
                row = int(pos[1] // SQUARE_SIZE)
                col = int(pos[0] // SQUARE_SIZE)

                game.mark(row, col) 
                game.switchPlayer()

        if (cont):
            drawBoard(game)
            pygame.display.update()


def main():

    #Introduction
    print("Let's play tic-tac-toe!")
    print("Use -help if you are stuck!")

    game = Game()

    while True:
        
        cmd = input()

        match cmd:
            
            case '-help':
                print('-ai: toggle ai')
                print('-i: play on gui')
                print('-t: play in terminal')
            
            #Toggle ai
            case '-ai':
                if (not game.exists()):
                    print('Game does not exist!')

            case '-i':
                pass
            
            case '-t':
                print()
                print("To play a move, pick a square number (1-9).")
                print()
                terminalEngine(game)

            case _:
                print('Unknown command :(')
    


main()
