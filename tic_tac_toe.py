import sys
import pygame
from pygame import gfxdraw

from game import Game
from ai import AI
from constants import * 

#Initialization 
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('<Tic-Tac-Toe>')
screen.fill(BOARD_COLOR)


def drawLines():

    #Horizontal
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

    #Vertical
    for j in range(1, COLS):
        pygame.draw.line(screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def drawBoard(game):
    
    board = game.board

    for row, col, player in board.fetch():

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
    
game = Game()
ai = AI(1)

time = 0

def main():

    time = 0
    while True:

        drawLines()
        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos = event.pos
                row = int(pos[1] // SQUARE_SIZE)
                col = int(pos[0] // SQUARE_SIZE)


                game.mark(row, col)
                cost, move = ai.findMove(game)
                row, col = move
                game.mark(row, col)
                

        drawBoard(game)
        pygame.display.update()

        
main()
