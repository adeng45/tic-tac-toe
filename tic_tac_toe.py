import sys
import pygame
import numpy as np

from constants import * 

#Initialization 
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('<Tic-Tac-Toe?')
screen.fill(BOARD_COLOR)


def main():

    while True:

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

        pygame.display.update()

main()
