import sys
import pygame

from game import Game
from ai import AI
from constants import * 

#Initialization 
def pygameInit():
    pygame.init()
    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption('<Tic-Tac-Toe>')
    return screen

def colorBoard(screen, color):
    screen.fill(BOARD_COLOR)

def drawLines(screen):

    #Horizontal
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

    #Vertical
    for j in range(1, COLS):
        pygame.draw.line(screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def drawBoard(screen, game):
    
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

def terminalEngine(game, ai):

    vspace()
    print("To play a move, pick a square number (1-9).")
    vspace()

    while (not game.isOver()):
        
        vspace()
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

    
    game.board.show()
    print('Player {0} wins!'.format(game.board.winner()))
    game.board.clear()
    game.switchPlayer()

def GUIEngine(game, ai):

    screen = pygameInit()
    colorBoard(screen, BOARD_COLOR)
    drawLines(screen)

    if (not game.firstMove):
        game.switchPlayer()
        move = ai.getMove(game)
        game.mark(move[0], move[1])
        game.switchPlayer()

    while (not game.isOver()):
        
        drawBoard(screen, game)
        pygame.display.update()

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                pygame.quit()
                return

            if (event.type == pygame.MOUSEBUTTONDOWN):
                pos = event.pos
                row = int(pos[1] // SQUARE_SIZE)
                col = int(pos[0] // SQUARE_SIZE)

                if (game.board.isSquareEmpty(row, col)):
                    game.mark(row, col) 
                    game.switchPlayer()

                    if (game.ai):
                        move = ai.getMove(game)
                        game.mark(move[0], move[1])
                        game.switchPlayer()

    drawBoard(screen, game)
    pygame.display.update()

    print('Player {0} wins!'.format(game.board.winner()))
    game.board.clear()

    pygame.quit()


def main():

    game = Game()
    ai = AI()

    while True:

        #Introduction
        vspace()
        print("Let's play tic-tac-toe!")
        print("Use -help for controls!")
        
        cmd = input()

        match cmd:
            
            case '-help':
                vspace()
                print('-g: play with GUI')
                print('-t: play in terminal')
                print('-s: change settings')
                print('-e: exit')


            case '-g':
                GUIEngine(game, ai)
            
            case '-t':
                terminalEngine(game, ai)
            
            case '-s':
                vspace()
                print('Change player 1, enter X or O.')
                print('Change move order, enter 1 or 2.')
                print('Turn on AI and set difficulty, enter -ai 1/-ai 2. Enter -ai 0 to turn off.')
                print('Autoplay, enter -a. Enter -a -s to turn off.')
                print('Enter -s to exit settings')

                cmd = None

                while (True):

                    cmd = input()

                    if (cmd == 'X' or cmd == 'O'):
                        if (not game.nextToMove() == cmd):
                            game.switchPlayer()
                        vspace()
                        print('Player 1 is now {0}!'.format(cmd))
                    
                    elif (cmd == '1' or cmd == '2'):

                        isLast = int(cmd) - 1
                        game.setFirstMove(isLast)
                        vspace()
                        print('Player 1 now goes {}!'.format('last' if isLast else 'first'))

                    elif (cmd == '-ai 0' or cmd == '-ai 1' or cmd == '-ai 2'):

                        difficulty = int(cmd.split(' ')[1])
                        if (difficulty == 0):
                            game.ai = False
                            vspace()
                            print('AI is turned off.')
                        else:
                            game.ai = True
                            ai.changeLevel(difficulty)
                            vspace()
                            print('AI {} is now your opponent!'.format('Brainless' if difficulty == 1 else 'AlphaZero'))

                    elif (cmd == '-a' or cmd == '-a -s'):
                        if (cmd == '-a'):
                            game.autoplay = True
                        else:
                            game.autoplay = False
                        vspace()
                        print('Autoplay turned {}!'.format('on' if cmd == '-a' else 'off'))

                    elif (cmd == '-s'):
                        break

                    else:
                        print('Unknown command :(')                        

            case '-e':
                sys.exit('Until next time!')

            case _:
                vspace()
                print('Unknown command :(')

main()